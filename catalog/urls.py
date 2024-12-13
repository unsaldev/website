"""
from django.urls import path
from .views import ExampleAPIView  # views.py'deki APIView'yi import et

urlpatterns = [
    path('example/', ExampleAPIView.as_view(), name='example-api'),
]
"""