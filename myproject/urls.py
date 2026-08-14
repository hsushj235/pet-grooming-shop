from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from core import views
import os

def serve_public_files(request, path):
    from django.http import FileResponse
    public_dir = os.path.join(settings.BASE_DIR, 'frontend', 'public')
    full_path = os.path.join(public_dir, path)
    if os.path.isfile(full_path):
        return FileResponse(open(full_path, 'rb'), as_attachment=False)
    from django.http import Http404
    raise Http404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('api/booking/', views.api_submit_booking, name='api_booking'),
    path('api/bookings/', views.api_list_bookings, name='api_bookings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static('/assets/', document_root=str(settings.BASE_DIR / 'frontend' / 'dist' / 'assets'))
    urlpatterns += static('/', document_root=str(settings.BASE_DIR / 'frontend' / 'public'), show_indexes=False)
