from django.urls import path
from homepage.views import index

app_name = 'homepage'

urlpatterns = [
    path('', index, name='index'),
]