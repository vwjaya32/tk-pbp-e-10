from importlib.resources import contents
from nntplib import ArticleInfo
from django.shortcuts import render
from django.shortcuts import redirect
from requests import request
from articles.models import *
from django import forms
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
import datetime

from django.views.decorators.csrf import csrf_exempt
import json as JSON

# Import forms
# ------------
from .forms import edit_box
from .forms import comment_box


# Functions for default user
# --------------------------
def show_articles(request):
    articles_list = Articles.objects.all()
    forms = edit_box(request.POST)
    context = {
        'data': articles_list,
        'form': forms,
    }
    return render(request, "articles.html", context)

def read_articles(request, id):
    theObject_a=Articles.objects.get(id=id)
    theObject_c=Comments.objects.filter(artc_place=theObject_a)
    context = {
        'target': theObject_a,
        'comment': theObject_c,
    }
    return render(request, "read.html", context)

def write_comments(request, id):
    if request.method == "POST":
        forms = comment_box(request.POST)
        if forms.is_valid():
            new_artc = Comments(
                author = forms.cleaned_data["author"],
                content = forms.cleaned_data["content"],
                artc_place = Articles.objects.get(id=id),
            )
            new_artc.save()
            return redirect("articles:read_articles", id)

    forms = comment_box()
    artc_data = Articles.objects.get(id=id)
    context={"form":forms, "the_artc":artc_data}
    return render(request, "write_cmt.html", context)


# Restricted functions; only for superuser
# ----------------------------------------
@user_passes_test(lambda u: u.is_superuser)
def write_articles(request):
    if request.method == "POST":
        forms = edit_box(request.POST)
        if forms.is_valid():
            new_artc = Articles(
                title = forms.cleaned_data["title"],
                author = forms.cleaned_data["author"],
                content = forms.cleaned_data["content"],
            )
            new_artc.save()
            return redirect("articles:show_articles")

    forms = edit_box()
    context={"form":forms}
    return render(request, "articles.html", context)

@user_passes_test(lambda u: u.is_superuser)
def delete_articles(request, id):
    Articles.objects.get(id=id).delete()
    return redirect("articles:show_articles")

@user_passes_test(lambda u: u.is_superuser)
def delete_comments(request, article_id, id):
    Comments.objects.get(id=id).delete()
    return redirect("articles:read_articles", article_id)

@user_passes_test(lambda u: u.is_superuser)
def add_ajax(request):
    form = edit_box()
    if request.method == "POST":
        form = edit_box(request.POST)
        if form.is_valid():
            new_artc = Articles(
                title = form.cleaned_data["title"],
                author = form.cleaned_data["author"],
                content = form.cleaned_data["content"],
            )
            new_artc.save()
        data = {
            "fields":{
                "title":form.cleaned_data["title"],
                "author":form.cleaned_data["author"],
                "date": datetime.date.today(),
                "content":form.cleaned_data["content"],
            },
            "pk":new_artc.pk
        }
        return JsonResponse(data)


# Data Delivery
# -------------
def show_json_articles(request):
    data = Articles.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_comments(request):
    data = Comments.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_comments_id(request, id):
    a = Articles.objects.get(id=id)
    data = Comments.objects.filter(artc_place=a)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def write_articles_flutter(request):
    if request.method == "POST":
        form = JSON.loads(request.body)
        # form = edit_box(request.POST)

        new_artc = Articles(
            title = form["title"],
            author = form["author"],
            content = form["content"],
        )
        new_artc.save()

        data = {
            "fields":{
                "title":form["title"],
                "author":form["author"],
                "date": datetime.date.today(),
                "content":form["content"],
            },
            "pk":new_artc.pk
        }
        return JsonResponse({"instance": "Success!"}, status=200)

@csrf_exempt
def write_comments_flutter(request, artc_id):
    if request.method == "POST":
        forms = JSON.loads(request.body)

        new_cmts = Comments(
            author = forms["author"],
            content = forms["content"],
            artc_place = Articles.objects.get(id=artc_id),
        )
        new_cmts.save()

        # return redirect("articles:read_articles", id)
        return JsonResponse({"instance": "Success!"}, status=200)

    # forms = comment_box()
    # artc_data = Articles.objects.get(id=id)
    # context={"form":forms, "the_artc":artc_data}
    # return render(request, "write_cmt.html", context)