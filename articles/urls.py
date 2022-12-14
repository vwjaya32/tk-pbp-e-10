from django.urls import path
from articles.views import *

app_name = 'articles'

urlpatterns = [
    path('', show_articles, name='show_articles'),
    path('delete-articles/<int:id>', delete_articles, name='delete_articles'),
    path('read/<int:id>', read_articles, name='read_articles'),
    path('comment/<int:id>', write_comments, name='write_comments'),
    path('delete-comments/<int:article_id>/<int:id>', delete_comments, name='delete_comments'),

    path('json-artc', show_json_articles, name='show_json_articles'),
    path('json-cmts', show_json_comments, name='show_json_comments'),
    path('json-cmts/<int:id>', show_json_comments_id, name='show_json_comments_id'),

    path('write-a-flutter',  write_articles_flutter, name='write_articles_flutter'),
    path('write-c-flutter/<int:artc_id>',  write_comments_flutter, name='write_comments_flutter'),

    path('delete-a-flutter/<int:id>',  delete_articles_flutter, name='delete_articles_flutter'),
    path('delete-c-flutter/<int:article_id>/<int:id>',  delete_comments_flutter, name='delete_comments_flutter'),

    path("add-ajax/", add_ajax, name="add_ajax"),
]