from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Shop
from .serializer import ShopSerializer

# Create your views here.


@api_view(['POST', 'GET'])
def create_list_shop(request):

    if request.method == 'POST':

        serializer = ShopSerializer(data=request.data)

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

    elif request.method == 'GET':

        shops = Shop.objects.all()

        serializer = ShopSerializer(shops, many=True)

        return Response({
            'count': shops.count(),
            'msg': 'list',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detail_delete_update_shop(request, pk):

    def get_object():
        shop = Shop.objects.filter(pk=pk).first()

        if not shop:
            raise ValidationError({
                'msg': 'Shop not found',
                'status': status.HTTP_400_BAD_REQUEST
            })

        return shop

    if request.method == 'GET':

        serializer = ShopSerializer(get_object())

        return Response({
            'msg': 'detail',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    elif request.method == 'PUT':

        serializer = ShopSerializer(
            instance=get_object(),
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': 'updated',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    elif request.method == 'PATCH':

        serializer = ShopSerializer(
            instance=get_object(),
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': 'updated',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    elif request.method == 'DELETE':

        get_object().delete()

        return Response({
            'msg': 'deleted',
            'status': status.HTTP_204_NO_CONTENT
        })

