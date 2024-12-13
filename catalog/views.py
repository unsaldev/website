# catalog/views.py
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ExampleAPIView(APIView):
    def get(self, request):
        data = {"message": "Hello, world!"}
        return Response(data, status=status.HTTP_200_OK)
"""
from django.views.generic import TemplateView

class ReactAppView(TemplateView):
    template_name = 'index.html'
