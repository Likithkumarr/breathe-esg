from django.shortcuts import render
from audit.models import AuditLog
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from normalization.models import NormalizedEmission


class ReviewDataView(APIView):

    def get(self, request):

        records = NormalizedEmission.objects.all()

        data = []

        for record in records:

            data.append({
                "id": record.id,
                "category": record.category,
                "activity_type": record.activity_type,
                "activity_value": record.activity_value,
                "unit": record.unit,
                "normalized_unit": record.normalized_unit,
                "approved": record.approved,
            })

        return Response(data)
class ApproveRecordView(APIView):

    def post(self, request, record_id):

        try:

            record = NormalizedEmission.objects.get(id=record_id)

            action = request.data.get('action')

            old_status = record.status
            if action == 'approve':
                record.approved = True
                record.status = 'approved'

            elif action == 'reject':
                record.approved = False
                record.status = 'rejected'

            record.save()

            AuditLog.objects.create(
                row_id=record.id,
                action=action,
                old_value={"status": old_status},
                new_value={"status": record.status},
                changed_by="analyst"
            )
            return Response({
                "message": f"Record {action}d successfully"
            })

        except NormalizedEmission.DoesNotExist:

            return Response({
                "error": "Record not found"
            }, status=404)