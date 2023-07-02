from django.db import models
from dry_rest_permissions.generics import allow_staff_or_superuser, authenticated_users


class BasePermissions:
    def has_read_permission(self):
        return True

    def has_object_read_permission(self):
        return True

    @allow_staff_or_superuser
    @authenticated_users
    def has_write_permission(self):
        return False

    @allow_staff_or_superuser
    @authenticated_users
    def has_object_write_permission(self):
        return False


# Create your models here.
class Restaurant(models.Model, BasePermissions):
    id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=35)
    short_description = models.CharField(max_length=60)
    restaurant_image = models.ImageField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.restaurant_name}"


class MenuCategory(models.Model, BasePermissions):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category}"


class Dish(models.Model, BasePermissions):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ManyToManyField(MenuCategory)
    dish_name = models.CharField(max_length=30)
    dish_image = models.ImageField()

    def __str__(self):
        return f"{self.dish_name}"


class FeaturedMenuCategory(models.Model, BasePermissions):
    id = models.AutoField(primary_key=True)
    featured = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.featured.category}"
