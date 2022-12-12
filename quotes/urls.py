from django.urls import path

# Import from views
from .views import *

app_name = 'quotes'

urlpatterns = [
    path('', show_html, name='show_html'),
    path('get_image', get_image, name='get_image'),
    path('get_image_user', get_image_user, name='get_image_user'),
    path('delete_image/<int:id>', delete_image, name='delete_image'),
    path('ajax_add_quote', ajax_add_quote, name="ajax_add_quote"),
    path('mob_add_quote', mob_add_quote, name="mob_add_quote"),
]
