from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
urlpatterns = [
    path('', include('Budget.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
