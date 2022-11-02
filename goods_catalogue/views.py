from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from goods_catalogue.models import *
from .models import *

def show_catalogue(request):
    return render(request, "catalogue.html")

def get_catalogue(request):
    catalogue_items = Catalogue.objects.all()
    return HttpResponse(
        serializers.serialize(
            "json", 
            catalogue_items, 
            use_natural_foreign_keys=True,
            ), 
        content_type="application/json")
