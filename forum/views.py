from django.shortcuts import render
from forum.models import *
# Create your views here.

def show_posts(request):
    all_posts = Posts.objects.all()
    context = {
        'data': all_posts,
    }
    return render(request, "forum.html", context)