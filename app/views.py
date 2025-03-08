from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from app.models import Region, Shop
from app.serializers import RegionSerializer, ShopSerializer


# Create your views here.

class RegionModelViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ShopApiViewSet(ViewSet):

    def list(self, request):
        data = Shop.objects.all()
        serializer = ShopSerializer(data, many=True)
        return Response({
            "count": len(serializer.data),
            "data": serializer.data
        })

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "created": True,
                "status": 200,
                "data": serializer.data
            }, status=200)
        return Response({
            "message": "Ошибка при валидации",
            "errors": serializer.errors
        }, status=400)

    def retrieve(self, request, pk=None):
        shop = Shop.objects.filter(id=pk).first()
        if shop:
            serializer = ShopSerializer(shop)
            return Response(serializer.data, 200)
        return Response({"message": "not found!"}, 404)








