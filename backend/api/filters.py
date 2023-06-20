import django_filters.rest_framework as filters

from recipes.models import Recipe, Ingredient, Tag


class RecipeFilter(filters.FilterSet):
    """Фильтр по избранному, автору, списку покупок и тегам"""
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=Tag.objects.all(),
        to_field_name="slug",
    )
    is_favorited = filters.BooleanFilter(method='filter_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='filter_is_in_shopping_cart')

    class Meta:
        model = Recipe
        fields = ['tags', 'author', 'is_favorited', 'is_in_shopping_cart']

    def filter_is_favorited(self, queryset, name, value):
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return Recipe.objects.all()

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if value:
            return queryset.filter(
                shopping_cart__user=self.request.user)
        return Recipe.objects.all()


class IngredientSearchFilter(filters.FilterSet):
    """Фильтр по частичному вхождению в начале названия ингредиента"""
    name = filters.CharFilter(
        field_name="name",
        lookup_expr="istartswith",
    )

    class Meta:
        model = Ingredient
        fields = ['name']
