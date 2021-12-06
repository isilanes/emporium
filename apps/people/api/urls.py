from django.urls import path, include

from apps.people.api.routers import router


app_name = "people"


urlpatterns = [
    path("", include(router.urls)),
]