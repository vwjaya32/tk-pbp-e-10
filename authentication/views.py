from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from homepage.models import *
from django.contrib.auth.models import User
from homepage.models import Customer

# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        register_as = request.POST.get('register_as')

        if password1 != password2:
            return JsonResponse({'status': False, 'message': 'Password tidak sesuai'}, status=400)
        
        try:
            user = User.objects.create_user(username=username, password=password1, email=None)
        except:
            return JsonResponse({'status': False, 'message': 'username invalid'}, status=400)
        
        try:
            customer = Customer.objects.get(user=user)
        except:
            customer = Customer.objects.create(
                user=user, 
                name=user.get_username(), 
                email="None", 
                phone="None",
                is_admin=register_as == "Admin"
            )
        return JsonResponse({'status': True}, status=200)

@csrf_exempt
def mob_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            customer = Customer.objects.filter(user=user)
            query_cust = customer.values()
            # Redirect to a success page.
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                "user": list(query_cust)[0],
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)
        
@csrf_exempt
def mob_logout(request):
    logout(request)
    return JsonResponse({
        'status': True,
        'message': 'Successfully Logged Out!',
    }, status=200)

def mob_get_user(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'status': True,
            'data': {
                'username': request.user.username,
            },
            'message': 'You are logged in',
        }, status=200)
    else:
        return JsonResponse({
            'status': False,
            'message': 'You are not logged in',
        }, status=200)
        
