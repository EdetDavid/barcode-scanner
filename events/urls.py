from rest_framework.routers import DefaultRouter
from .views import EventsViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'events', EventsViewSet, basename='events')


urlpatterns = [
    path('api/', include(router.urls)),
]
