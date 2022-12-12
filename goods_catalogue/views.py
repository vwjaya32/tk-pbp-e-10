import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from goods_catalogue.models import *
from homepage.models import *
from .models import *
from .forms import *
from mycart.models import *
from itertools import chain

@login_required(login_url='/login')
def show_catalogue(request):
    context = {
        'forms': ItemForm(),
        'customer': Customer.objects.get(user=request.user)}
    return render(request, "catalogue.html", context)

@login_required(login_url='/login')
def get_catalogue(request):
    catalogue_items = Catalogue.objects.all()
    # return HttpResponse(
        # serializers.serialize(
        #    "json", 
        #    catalogue_items, 
        #    use_natural_foreign_keys=True,
        #    ), 
    serialized_queryset = serializers.serialize('python', catalogue_items)
    return JsonResponse(serialized_queryset, safe=False, status=200)

@login_required(login_url='/login/')
@csrf_exempt
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
                comfortrate=request.POST.get('comfortrate'),
                image=image)
        elif type == "HappinessBooster":
            item = HappinessBoost.objects.create(
                name=name+" (Happiness Booster)",
                price=price,
                boostrate=request.POST.get('boostrate'),
                image=image)

        return HttpResponse(
            serializers.serialize(
                "json", 
                {item.get_parent()}, 
                use_natural_foreign_keys=True,
                ), 
            content_type="application/json",
            status=200)

@login_required(login_url='/login/')
@csrf_exempt
def add_to_cart(request, pk):
    product = Catalogue.objects.get(pk=pk)
    customer = Customer.objects.get(user=request.user)
    print(customer.name)
    myorder = Order.objects.get_or_create(customer=customer, is_complete=False, on_process=False)
    try:
        order_item = OrderItem.objects.get(product=product, order=myorder[0].id)
    except OrderItem.DoesNotExist:
        order_item = OrderItem.objects.create(
            product=product,
            order=myorder[0],
            quantity=1,
        )
    else:
        order_item.quantity += 1
        order_item.save()
   
    return JsonResponse({'status':'200'})
    
    # return HttpResponse(
    #         serializers.serialize(
    #             "json", 
    #             order_item, 
    #             use_natural_foreign_keys=True,
    #             ), 
    #         content_type="application/json")

