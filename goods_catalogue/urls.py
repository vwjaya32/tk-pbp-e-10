
from django.urls import path
from .views import *

app_name = 'goods_catalogue'

urlpatterns = [
    path('', show_catalogue, name='catalogue'),
    path('get_catalogue/', get_catalogue, name="get_catalogue"),
    path('add_item/', add_item, name="add_item"),
    path('add_to_cart/<int:pk>', add_to_cart, name="add_to_cart"),
] 