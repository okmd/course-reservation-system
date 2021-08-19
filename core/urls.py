
from django import contrib
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
