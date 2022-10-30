from django.urls import path
from mh_tests.views import *

app_name = 'mh_tests'

urlpatterns = [
    path('', mhtestpage, name='mhtestpage'),
    path('add/', save_points, name='save_points'),
    path('json/', json_res, name='json_res'),
    path('delete_res/<int:pk>', delete_res, name='delete_res'),
    
]