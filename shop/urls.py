from django.urls import path
from .views import *

urlpatterns = [
    path(
        'create-list/',
        CreateListShopAPIView.as_view()
    ),
    path(
        'detail-delete-update/<int:pk>/',
        DetailDeleteUpdateShopAPIView.as_view()
    ),
]