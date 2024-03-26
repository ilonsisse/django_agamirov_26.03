from django.contrib import admin
from .models import (Place, Shop)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'supervisor', 'place', 'is_open')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')
# Register your models here.
