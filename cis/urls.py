from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('cis/cis/admin/', admin.site.urls),
    
    path('cis/cis/', include('city_school.urls')),
    
    path('', include('pwa.urls')),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)