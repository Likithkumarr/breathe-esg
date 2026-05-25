from django.urls import path
from .views import ReviewDataView, ApproveRecordView

urlpatterns = [
    path('review/', ReviewDataView.as_view()),
    path('review/<int:record_id>/', ApproveRecordView.as_view()),
]