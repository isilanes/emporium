from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = [
    # Admin interface:
    path('admin/', admin.site.urls),

    # REST API interface:
    path('api/garage/', include('apps.garage.api.urls', namespace="api-garage")),
]

for app in settings.EXTRA_APPS:
    app_name = app.split(".")[-1]  # if app = "apps.app_name", "fix" it
    urlpatterns.append(path(f'{app_name}/', include(f'{app}.urls', namespace=app_name)))
