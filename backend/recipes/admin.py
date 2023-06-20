from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html


from .models import (FavoriteRecipe, Ingredient, Recipe,
                     RecipeIngredient, ShoppingCart, Tag)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    min_num = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'color', 'slug',)
    search_fields = ('name',)
    ordering = ('color',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'image_tag', 'amount_favorites',)
    search_fields = ('name',)
    list_filter = ('name', 'author', 'tags',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY
    inlines = [
        RecipeIngredientInline,
    ]

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="70" />'.format(
            obj.image.url))
    image_tag.short_description = 'Картинка'

    @staticmethod
    @admin.display()
    def amount_favorites(obj):
        return obj.favorites.count()


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'amount',)
    list_filter = ('id', 'recipe', 'ingredient',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe',)
    search_fields = ('user', 'recipe',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe',)
    search_fields = ('user', 'recipe',)
    list_filter = ('user',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY
