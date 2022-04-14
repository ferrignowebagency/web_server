from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('lead.urls')),
    path('api/v1/', include('agency.urls')),
    path('api/v1/', include('clients.urls')),
    path('api/v1/', include('annunci.urls')),
]
