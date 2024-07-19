from .views import *
from django.urls import path

urlpatterns = [
    path('cat/', CatViewSets.as_view({'get': 'list', 'post': 'create'}), name='cat_list'),
    path('cat/<int:pk>', CatViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='cat_detail'),

    path('product/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('product/<int:pk>', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail')

]
