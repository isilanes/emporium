from rest_framework import routers

from apps.people.api import views


router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)
