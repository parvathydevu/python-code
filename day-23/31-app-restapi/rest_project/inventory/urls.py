from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsumableViewSet

router = DefaultRouter()
router.register(r'consumables', ConsumableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]