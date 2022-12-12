from unicodedata import name
from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_posts, name='show_posts'),
    path('read/<int:id>/', read_forum, name='read_forum'),
    path('start-forum/', new_forum, name='new_forum'),
    path('json/', show_forum_json, name='show_forum_json'),
    path('json/<int:id>/', show_json_id, name='show_json_id'),
    path('comment/<int:id>/', reply_thread, name='reply_thread'),
    path("get-forum-flutter/", show_forum_json_flutter, name="show_forum_json_flutter"),
    path("add-forum-flutter/", add_forum_flutter, name="add_stories_flutter"),
    path("get-replies-flutter/", show_replies_json_flutter, name="show_replies_json_flutter"),
    path("add-replies-flutter/", add_replies_flutter, name="add_replies_flutter"),
]