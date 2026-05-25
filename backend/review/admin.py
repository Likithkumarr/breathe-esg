from django.contrib import admin

# Register your models here.
from django.contrib import admin
from audit.models import AuditLog
admin.site.register(AuditLog)