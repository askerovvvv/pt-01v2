from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import RegionModelViewSet, ShopApiViewSet, SavedCreateListApiView

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
    })),
    path('saved/', SavedCreateListApiView.as_view())
]

