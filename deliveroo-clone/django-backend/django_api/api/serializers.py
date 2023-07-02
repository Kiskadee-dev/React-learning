from rest_framework import serializers
from .models import Restaurant, MenuCategory, Dish, FeaturedMenuCategory


class RestaurantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "restaurant_name",
            "short_description",
            "restaurant_image",
            "latitude",
            "longitude",
        ]


class MenuCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = MenuCategory
        fields = ["id", "category"]


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ["restaurant", "category", "dish_name", "dish_image"]


class FeaturedMenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedMenuCategory
        fields = ["featured"]
