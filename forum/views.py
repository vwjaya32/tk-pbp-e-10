from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from forum.models import *
from django import forms
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def show_posts(request):
    all_posts = Posts.objects.all()
    context = {
        'data': all_posts,
    }
    return render(request, "forum.html", context)

class make_box(forms.Form):
    author = forms.CharField(label="Author", widget=forms.TextInput(attrs={'size': 37}))
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'size': 37}))
    content = forms.CharField(label="Content", widget=forms.Textarea)

class reply_box(forms.Form):
    author = forms.CharField(label="Author", widget=forms.TextInput(attrs={'size': 37}))
    content = forms.CharField(label="Content", widget=forms.Textarea)

def read_forum(request, id):
    forum_posts=Posts.objects.get(id=id)
    forum_comments=Replies.objects.filter(posts_index=forum_posts)
    context = {
        'thread': forum_posts,
        'comment': forum_comments,
    }
    return render(request, "read_posts.html", context)

def new_forum(request):
    if request.method == "POST":
        forms = make_box(request.POST)
        if forms.is_valid():
            posted = Posts(
                title = forms.cleaned_data["title"],
                author = forms.cleaned_data["author"],
                content = forms.cleaned_data["content"],
            )
            posted.save()
            return redirect("forum:show_posts")
    forms = make_box()
    context={"form":forms}
    return render(request, "write_forum.html", context)

@login_required(login_url='/login/')
def reply_thread(request, id):
    if request.method == "POST":
        forms = reply_box(request.POST)
        if forms.is_valid():
            reply_posted = Replies(
                author = forms.cleaned_data["author"],
                content = forms.cleaned_data["content"],
                posts_index = Posts.objects.get(id=id),
            )
            reply_posted.save()
            return redirect("forum:read_forum", id)

    forms = reply_box()
    post_data = Posts.objects.get(id=id)
    context={"form":forms, "posts":post_data, 'username': request.user}
    return render(request, "write_reply.html", context)

def show_forum_json(request):
    data = Posts.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_id(request, id):
    data = Posts.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")