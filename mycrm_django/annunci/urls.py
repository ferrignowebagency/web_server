from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AnnunciViewSet

router = DefaultRouter()
router.register('annunci', AnnunciViewSet, basename='annunci')

urlpatterns = [
    path('', include(router.urls)),
]