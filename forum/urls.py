from unicodedata import name
from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_posts, name='show_posts'),
    path('read/<int:id>/', read_forum, name='read_forum'),
    path('start-forum/',new_forum, name='new_forum'),
    path('json/', show_forum_json, name='show_forum_json')
]