from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', mob_login, name='mob_login'),
    path('logout/', mob_logout, name='mob_logout'),
    path('user/', mob_get_user, name='mob_get_user'),  
]