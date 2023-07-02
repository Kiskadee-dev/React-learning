from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from dry_rest_permissions.generics import DRYPermissions
from .models import Restaurant, MenuCategory, Dish, FeaturedMenuCategory
from .serializers import (
    RestaurantSerializer,
    MenuCategorySerializer,
    DishSerializer,
    FeaturedMenuCategorySerializer,
)


class RestaurantsViewSet(viewsets.ModelViewSet):
    """
    Endpoint dos restaurantes
    """

    queryset = Restaurant.objects.all()  # noqa
    serializer_class = RestaurantSerializer
    permission_classes = [DRYPermissions]


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()  # noqa
    serializer_class = MenuCategorySerializer
    permission_classes = [DRYPermissions]


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()  # noqa
    serializer_class = DishSerializer
    permission_classes = [DRYPermissions]


class FeaturedMenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = FeaturedMenuCategory.objects.all()  # noqa
    serializer_class = FeaturedMenuCategorySerializer
    permission_classes = [DRYPermissions]
