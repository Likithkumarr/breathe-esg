from django.urls import path
from .views import NormalizeDataView

urlpatterns = [
    path('normalize/', NormalizeDataView.as_view()),
]