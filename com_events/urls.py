from django.urls import path
from com_events.views import *

app_name = "com_events"

urlpatterns = [
    path('', show_events, name='show_events'),
    path('add_event', add_event, name='add_event'),
    path('delete/<int:id>', delete, name='delete'),
    path('join_event/<int:id>', join_event, name='join_event'),
    path('unjoin_event/<int:id>', unjoin_event, name='unjoin_event'),
    path('register/', register_temp, name='register'), 
    path('login/', login_user_temp, name='login'),
    path('logout/', logout_user_temp, name='logout'),
]