from django.db import models

# Create your models here.
from django.db import models
from ingestion.models import RawRecord

class NormalizedEmission(models.Model):

    CATEGORY_CHOICES = [
        ('scope1', 'Scope 1'),
        ('scope2', 'Scope 2'),
        ('scope3', 'Scope 3'),
    ]

    raw_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE
    )

    category = models.CharField(max_length=20)

    activity_type = models.CharField(max_length=100)

    activity_value = models.FloatField()

    unit = models.CharField(max_length=50)

    normalized_unit = models.CharField(max_length=50)

    emission_factor = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        default='normalized'
    )

    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)