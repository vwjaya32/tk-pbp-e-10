from django.urls import path
from mh_tests.views import *

app_name = 'mh_tests'

urlpatterns = [
    path('', mhtestpage, name='mhtestpage'),
    
]