from django.urls import path
from articles.views import *

app_name = 'articles'

urlpatterns = [
    path('', show_articles, name='show_articles'),
    path('write-news/', write_articles, name='write_articles'),
    path('delete/<int:id>', delete_articles, name='delete_articles'),
    path('read/<int:id>', read_articles, name='read_articles'),
]