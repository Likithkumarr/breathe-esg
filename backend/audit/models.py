from django.db import models

# Create your models here.
from django.db import models

class AuditLog(models.Model):

    row_id = models.IntegerField()

    action = models.CharField(max_length=100)

    old_value = models.JSONField(null=True, blank=True)

    new_value = models.JSONField(null=True, blank=True)

    changed_by = models.CharField(max_length=100)

    timestamp = models.DateTimeField(auto_now_add=True)