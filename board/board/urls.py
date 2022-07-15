from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from ads.views import load_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ads/', include('ads.urls')),
    path('posts/', include('news.urls')),
    path('', load_data)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)