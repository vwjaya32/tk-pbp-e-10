import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from homepage.models import *
from goods_catalogue.models import *
from homepage.forms import RegisterUserForm

def show_homepage(request):
    return render(request, 'homepage.html')


def register(request):
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                customer = Customer.objects.get(user=user)
            except:
                customer = Customer.objects.create(
                    user=user, 
                    name=user.get_username(), 
                    email="None", 
                    phone="None",
                    is_admin=form.cleaned_data['regist_as'] == "Adminf"
                )
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('homepage:login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    next_value = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_value:
                response = HttpResponseRedirect(next_value)
            else:
                response = HttpResponseRedirect(reverse("homepage:show_homepage"))
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('user', user.id) # membuat cookie last_login dan menambahkannya ke dalam response        
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('homepage:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('user') # membuat cookie last_login dan menambahkannya ke dalam response
    return response