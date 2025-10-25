from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('web.urls')),    
    path('', include('customers.urls')),
    path('stores/', include('stores.urls')),
    path('admin/', admin.site.urls),
    
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

