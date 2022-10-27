from django.urls import path
from com_events.views import *

urlpatterns = [
    path('', show_events, name='show_events'),
]