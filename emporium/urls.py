from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = [
    path("", include("apps.garage.urls", namespace="main")),

    # Admin interface:
    path('admin/', admin.site.urls),

    # REST API interface:
    path('api/garage/', include('apps.garage.api.urls', namespace="api-garage")),
    path('api/leases/', include('apps.leases.api.urls', namespace="api-leases")),
    path('api/people/', include('apps.people.api.urls', namespace="api-people")),
]

for app in settings.EXTRA_APPS:
    app_name = app.split(".")[-1]  # if app = "apps.app_name", "fix" it
    urlpatterns.append(path(f"{app_name}/", include(f"{app}.urls", namespace=app_name)))
