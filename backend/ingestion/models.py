from django.db import models

# Create your models here.
from django.db import models

class RawRecord(models.Model):
    SOURCE_CHOICES = [
        ('sap', 'SAP'),
        ('utility', 'Utility'),
        ('travel', 'Travel'),
    ]

    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    file_name = models.CharField(max_length=255)

    raw_data = models.JSONField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        default='uploaded'
    )

    suspicious = models.BooleanField(default=False)

    created_by = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.source_type} - {self.file_name}"