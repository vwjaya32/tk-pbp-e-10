from django.urls import path
from articles.views import *

app_name = 'articles'

urlpatterns = [
    path('', show_articles, name='show_articles'),
    path('write-news/', write_articles, name='write_articles'),
    path('delete-articles/<int:id>', delete_articles, name='delete_articles'),
    path('read/<int:id>', read_articles, name='read_articles'),
    path('comment/<int:id>', write_comments, name='write_comments'),
    path('delete-comments/<int:article_id>/<int:id>', delete_comments, name='delete_comments'),

    path('json-artc', show_json_articles, name='show_json_articles'),
    path("add-ajax/", add_ajax, name="add_ajax"),
]