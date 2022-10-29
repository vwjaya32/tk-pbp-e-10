from django.urls import path

# Import from views
from .views import show_html
from .views import add_quote
from .views import get_image

app_name = 'quotes'

urlpatterns = [
    path('', show_html, name='show_html'),
    path('add_quote', add_quote, name='add_quote'),
    path('get_image', get_image, name='get_image'),
]
