from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

for app in settings.EXTRA_APPS:
    app_name = app.split(".")[-1]  # if app = "apps.app_name", "fix" it
    urlpatterns.append(path(f'{app_name}/', include(f'{app}.urls', namespace=app_name)))
