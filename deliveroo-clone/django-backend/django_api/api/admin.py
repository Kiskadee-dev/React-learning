from django.contrib import admin
from .models import Restaurant, Dish, FeaturedMenuCategory, MenuCategory
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(FeaturedMenuCategory)
admin.site.register(MenuCategory)
