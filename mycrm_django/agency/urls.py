from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AgencyViewSet, UserDetail, get_my_agency, add_agent

router = DefaultRouter()
router.register('agency', AgencyViewSet, basename='agency')

urlpatterns = [
    path('agency/agent/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('agency/get_my_agency/', get_my_agency, name='get_my_agency'),
    path('agency/add_agent/', add_agent, name='add_agent'),
    path('', include(router.urls)),
]