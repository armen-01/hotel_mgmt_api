from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, GuestViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'guests', GuestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
