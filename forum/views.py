from django.shortcuts import render
from django.shortcuts import redirect
from forum.models import *
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
from django.core import serializers
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

def json(request):
    data = Posts.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")