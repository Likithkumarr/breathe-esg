import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from normalization.models import NormalizedEmission
from .models import RawRecord


class UploadCSVView(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        print("CONTENT TYPE:", request.content_type)
        print("FILES:", request.FILES)
        print("DATA:", request.data)

        uploaded_file = request.FILES.get('file')

        source_type = request.data.get('source_type')

        if not uploaded_file:
            return Response({
                "error": "No file uploaded"
            }, status=400)

        try:

            df = pd.read_csv(uploaded_file)

            saved_rows = []

            for row in df.to_dict(orient='records'):

                suspicious = False

                if 'quantity' in row:

                    try:
                        if float(row['quantity']) < 0:
                            suspicious = True
                    except:
                        pass

                raw_record = RawRecord.objects.create(
                    source_type=source_type,
                    file_name=uploaded_file.name,
                    raw_data=row,
                    suspicious=suspicious,
                    created_by="admin"
                )
                NormalizedEmission.objects.create(
                    raw_record=raw_record,
                    category="scope1",
                    activity_type=row.get("activity_type", "fuel combustion"),
                    activity_value=float(row.get("quantity", 0)),
                    unit=row.get("unit", "liters"),
                    normalized_unit=row.get("unit", "liters"),
                    approved=False
                )

                saved_rows.append(raw_record.id)

            return Response({
                "message": "CSV uploaded successfully",
                "rows_saved": len(saved_rows)
            })

        except Exception as e:

            return Response({
                "error": str(e)
            }, status=500)