from django.urls import path
from mh_goods.views import *

app_name = 'mh_goods'

urlpatterns = [
    path('', mhgoods, name='mhgoods'),
]