from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Shop
from .serializer import ShopSerializer

# Create your views here.


class CreateListShopAPIView(APIView):

    def get(self, request):

        shops = Shop.objects.all()

        serializer = ShopSerializer(
            shops,
            many=True
        )

        return Response({
            'count': shops.count(),
            'msg': 'list',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def post(self, request):

        serializer = ShopSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response({
                'msg': 'Created',
                'status': status.HTTP_201_CREATED,
                'data': serializer.data
            })

        raise ValidationError({
            'error': serializer.errors,
            'status': status.HTTP_400_BAD_REQUEST
        })


class DetailDeleteUpdateShopAPIView(APIView):

    def get_object(self, pk):

        shop = Shop.objects.filter(
            pk=pk
        ).first()

        if not shop:
            raise ValidationError({
                'msg': 'Shop not found',
                'status': status.HTTP_400_BAD_REQUEST
            })

        return shop

    def get(self, request, pk):

        serializer = ShopSerializer(
            self.get_object(pk)
        )

        return Response({
            'msg': 'detail',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def put(self, request, pk):

        serializer = ShopSerializer(
            instance=self.get_object(pk),
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response({
            'msg': 'updated',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def patch(self, request, pk):

        serializer = ShopSerializer(
            instance=self.get_object(pk),
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response({
            'msg': 'updated',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def delete(self, request, pk):

        self.get_object(pk).delete()

        return Response({
            'msg': 'deleted',
            'status': status.HTTP_204_NO_CONTENT
        })