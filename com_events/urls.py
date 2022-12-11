from django.urls import path
from com_events.views import *

app_name = "com_events"

urlpatterns = [
    path('', show_events, name='show_events'),
    path('list_events', list_events, name='list_events'),
    path('json_all/', get_json_all, name='json_all'),
    path('json_mobile', get_json_all_mobile, name='json_mobile'),
    path('json_user/', get_json_user, name='json_user'),
    path('delete/<int:id>', delete, name='delete'),
    path('join_event/<int:id>', join_event, name='join_event'),
    path('unjoin_event/<int:id>', unjoin_event, name='unjoin_event'),
    path('add/', add_event_ajax, name='add')
]