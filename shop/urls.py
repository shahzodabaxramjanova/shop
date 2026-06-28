from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ListShopAPIView.as_view()),
    path('create/', CreateShopAPIView.as_view()),
    path('detail/<int:pk>/', RetrieveShopAPIView.as_view()),
    path('update/<int:pk>/', UpdateShopAPIView.as_view()),
    path('delete/<int:pk>/', DestroyShopAPIView.as_view()),
]