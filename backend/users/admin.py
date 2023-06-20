from django.conf import settings
from django.contrib import admin

from .models import User, Follow


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email',
                    'first_name', 'last_name',)
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'user',)
    search_fields = ('author', 'user',)
    list_filter = ('author', 'user',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY
