from django.urls import path
from articles.views import *

app_name = 'articles'

urlpatterns = [
    path('', show_articles, name='show_articles'),
    path('write-news/', write_articles, name='write_articles'),
]