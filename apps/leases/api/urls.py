from django.urls import path, include

from apps.leases.api.routers import router


app_name = "leases"


urlpatterns = [
    path("", include(router.urls)),
]