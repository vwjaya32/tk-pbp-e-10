from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def mob_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                'data': {
                    'username': request.user.username,
                },
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
        
