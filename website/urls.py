from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # TemplateView'ı import ediyoruz
from catalog.views import ReactAppView  # ReactAppView'ı import ediyoruz

urlpatterns = [
    path("admin/", admin.site.urls),
   # path('', TemplateView.as_view(template_name='index.html'), name='home'),  # index.html'yi burada çağırıyoruz
    path('', ReactAppView.as_view(), name='home')
   # path("api/", include('catalog.urls')),  # catalog/urls.py'yi dahil ettik
]
