from rest_framework import routers
from . import views
from django.urls import include, path


router = routers.DefaultRouter()

router.register(r"Restaurants", views.RestaurantsViewSet)
router.register(r"MenuCategory", views.MenuCategoryViewSet)
router.register(r"Dish", views.DishViewSet)
router.register(r"FeaturedMenuCategory", views.FeaturedMenuCategoryViewSet)


urlpatterns = [
    path("api/", include(router.urls)),

]

#
