from django.urls import path, include

from apps.garage.api.routers import router


app_name = "garage"


urlpatterns = [
    path("", include(router.urls)),
]