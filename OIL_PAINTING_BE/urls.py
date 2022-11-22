from django.contrib import admin
from django.urls import path, include

# 사진
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('inquiries/', include('inquiries.urls')),
    path('painters/', include('painters.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)