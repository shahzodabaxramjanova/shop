from django.urls import path
from .views import *

urlpatterns = [
    path('create-list/', create_list_shop),
    path('detail-delete-update/<int:pk>/', detail_delete_update_shop),
]