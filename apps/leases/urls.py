from django.urls import path

from . import views


app_name = "leases"


urlpatterns = [
    path("", views.main, name="main"),
]