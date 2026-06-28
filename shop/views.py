from rest_framework import generics

from .models import Shop
from .serializer import ShopSerializer


class ListShopAPIView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CreateShopAPIView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class RetrieveShopAPIView(generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class UpdateShopAPIView(generics.UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class DestroyShopAPIView(generics.DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer