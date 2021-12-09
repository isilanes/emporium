from django.contrib import admin

from .models import Lease, LeaseTemplate


admin.site.register(Lease)
admin.site.register(LeaseTemplate)
