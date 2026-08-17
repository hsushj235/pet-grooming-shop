from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('api/booking/', views.api_submit_booking, name='api_booking'),
    path('api/bookings/', views.api_list_bookings, name='api_bookings'),
]
