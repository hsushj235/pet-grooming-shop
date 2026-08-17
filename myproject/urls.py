from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from core import views
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('api/booking/', views.api_submit_booking, name='api_booking'),
    path('api/bookings/', views.api_list_bookings, name='api_bookings'),
]

# 静态文件服务：包括 /assets/* 和 /static/*（使用 WhiteNoise）
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # 生产环境：添加 /assets/* 路由（WhiteNoise 会自动处理这些文件）
    from django.views.static import serve
    urlpatterns += [
        path('assets/<path:path>', serve, {'document_root': settings.STATIC_ROOT / 'assets'}),
        path('favicon.svg', serve, {'document_root': settings.STATIC_ROOT}),
    ]
