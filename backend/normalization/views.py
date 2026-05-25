from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from ingestion.models import RawRecord
from .models import NormalizedEmission


class NormalizeDataView(APIView):

    def post(self, request):

        raw_records = RawRecord.objects.all()

        normalized_count = 0

        for record in raw_records:

            data = record.raw_data

            quantity = float(data.get('quantity', 0))

            unit = data.get('unit', '')

            normalized_value = quantity

            normalized_unit = 'liters'

            # Example conversion
            if unit.lower() == 'gallons':
                normalized_value = quantity * 3.785

            NormalizedEmission.objects.create(
                raw_record=record,
                category='scope1',
                activity_type='fuel combustion',
                activity_value=normalized_value,
                unit=unit,
                normalized_unit=normalized_unit,
                status='normalized'
            )

            normalized_count += 1

        return Response({
            "message": "Normalization complete",
            "normalized_rows": normalized_count
        })