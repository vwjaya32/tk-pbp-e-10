from django.urls import path

# Import from views
from .views import *

app_name = 'quotes'

urlpatterns = [
    path('', show_html, name='show_html'),
    path('add_quote', add_quote, name='add_quote'),
    path('get_image', get_image, name='get_image'),
    path('delete_image/<int:id>', delete_image, name='delete_image'),
]
