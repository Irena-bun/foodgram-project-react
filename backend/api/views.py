from djoser.views import UserViewSet
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from django.db.models import Prefetch

from users.models import Follow, User
from recipes.models import (Tag, FavoriteRecipe, Ingredient,
                            Recipe, RecipeIngredient, ShoppingCart)
from .serializers import (CustomUserSerializer, FollowSerializer,
                          ShowFollowsSerializer, TagSerializer,
                          AddRecipeSerializer, ShowRecipeSerializer,
                          FavoriteRecipeSerializer, IngredientSerializer,
                          ShoppingCartSerializer)
from .permissions import IsAdminOrReadOnly, IsAuthorAdminOrReadOnly
from .filters import IngredientSearchFilter, RecipeFilter
from .services import convert_to_file


class CustomUserViewSet(UserViewSet):
    """Вьюсет для пользователя"""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly,]

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        url_path='subscribe',
        url_name='subscribe',
        permission_classes=[permissions.IsAuthenticated],
    )
    def subscribe(self, request, id):
        """Подписка/отписка на/от автора"""
        author = get_object_or_404(User, id=id)
        serializer = FollowSerializer(
            data={'user': request.user.id, 'author': id})
        if request.method == 'POST':
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            serializer = ShowFollowsSerializer(author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        follow = get_object_or_404(Follow, user=request.user, author__id=id)
        follow.delete()
        return Response(
            f'{request.user} отписался от {follow.author}',
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(
        detail=False,
        methods=['GET'],
        url_path='subscriptions',
        url_name='subscriptions',
        permission_classes=[permissions.IsAuthenticated],)
    def show_follows(self, request):
        """Просмотр подписок"""
        user_obj = User.objects.filter(following__user=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(user_obj, request)
        serializer = ShowFollowsSerializer(
            result_page, many=True, context={'current_user': request.user}
        )
        return paginator.get_paginated_response(serializer.data)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class IngredientViewSet(viewsets.ModelViewSet):
    """Вьюсет для ингредиентов"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientSearchFilter


class RecipeViewSet(viewsets.ModelViewSet):
    """Вьюсет для рецептов"""
    queryset = Recipe.objects.select_related('author').prefetch_related(
        Prefetch('ingredients', to_attr='tags',
                 queryset=RecipeIngredient.objects.select_related(
                     'ingredient'))
    )
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthorAdminOrReadOnly,)
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ShowRecipeSerializer
        return AddRecipeSerializer

    def __add_or_del_recipe(self, method, user, pk, model, serializer):
        """Добавление/удаление в избранное или список покупок"""
        recipe = get_object_or_404(Recipe, pk=pk)
        if method == 'POST':
            model.objects.get_or_create(user=user, recipe=recipe)
            return Response(
                serializer.to_representation(instance=recipe),
                status=status.HTTP_201_CREATED,
            )
        if method == 'DELETE':
            model.objects.filter(user=user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        url_path='favorite',
        url_name='favorite',
        permission_classes=[permissions.IsAuthenticated],
    )
    def favorite(self, request, pk):
        """Добавление/удаление в/из избранного"""
        return self.__add_or_del_recipe(
            request.method,
            request.user,
            pk,
            model=FavoriteRecipe,
            serializer=FavoriteRecipeSerializer(),
        )

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        url_name='shopping_cart',
        url_path='shopping_cart',
        permission_classes=[permissions.IsAuthenticated],
    )
    def shopping_cart(self, request, pk):
        """Добавление/удаление покупок в/из корзины"""
        return self.__add_or_del_recipe(
            request.method,
            request.user,
            pk,
            model=ShoppingCart,
            serializer=ShoppingCartSerializer(),
        )

    @action(
        detail=False,
        methods=['GET'],
        url_name='download_shopping_cart',
        url_path='download_shopping_cart',
        permission_classes=[IsAuthenticated,],
    )
    def download_shopping_cart(self, request):
        """Выгрузка списка покупок"""
        cart_ingredients = (
            RecipeIngredient.objects.filter(
                recipe__shopping_cart__user=request.user
            )
            .values(
                'ingredient__name',
                'ingredient__measurement_unit',
            )
            .annotate(ingredient_total_amount=Sum('amount'))
        )
        return convert_to_file(cart_ingredients)
