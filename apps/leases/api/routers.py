from rest_framework import routers

from apps.leases.api import views


router = routers.DefaultRouter()
router.register(r'lease', views.LeasesViewSet)
router.register(r'lease-templates', views.LeaseTemplatesViewSet)
