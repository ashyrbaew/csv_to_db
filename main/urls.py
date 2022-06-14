from django.urls import path, include
from rest_framework import routers
from .views import AircraftViewSet, StatusViewSet, TypeViewSet

app_name = 'main'

router = routers.SimpleRouter()

router.register('api/aircraft', AircraftViewSet, basename='aircraft')
router.register('api/status', StatusViewSet, basename='status')
router.register('api/type', TypeViewSet, basename='stotypere')

urlpatterns = [
    path('', include(router.urls)),
]