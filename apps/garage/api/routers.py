from rest_framework import routers

from apps.garage.api import views


router = routers.DefaultRouter()
router.register(r'garage', views.GarageViewSet)
