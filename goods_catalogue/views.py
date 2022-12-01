import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from goods_catalogue.models import *
from homepage.models import *
from .models import *
from .forms import *
from itertools import chain

def show_catalogue(request):
    context = {'forms': ItemForm()}
    return render(request, "catalogue.html", context)

def get_catalogue(request):
    catalogue_items = Catalogue.objects.all()
    return HttpResponse(
        serializers.serialize(
            "json", 
            catalogue_items, 
            use_natural_foreign_keys=True,
            ), 
        content_type="application/json")

@login_required(login_url='/login/')
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        price = request.POST.get('price')
        image = request.POST.get('image')
        if type == "Soul Comforter":
            item = SoulComforter.objects.create(
                name=name+" (Soul Comforter)",
                price=price,
                image=image)
        elif type == "Anxiety Boost":
            item = AnxietyBoost.objects.create(
                name=name+" (Anxiety Boost)",
                price=price,
                image=image)

        return HttpResponse(
            serializers.serialize(
                "json", 
                {item.get_parent()}, 
                use_natural_foreign_keys=True,
                ), 
            content_type="application/json")

