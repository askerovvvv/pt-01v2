from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import RegionModelViewSet, ShopApiViewSet

router = DefaultRouter()
router.register('', RegionModelViewSet)

urlpatterns = [
    path('region/', include(router.urls)),
    path('shop/', ShopApiViewSet.as_view({
        'get': 'list',
        'post': 'post'
    })),
    path('shop/<int:pk>', ShopApiViewSet.as_view({
        'get': 'retrieve'
    }))
]

