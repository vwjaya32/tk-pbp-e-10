from django.urls import reverse
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar, month_name
from datetime import datetime
from com_events.models import *
from com_events.forms import EventForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def show_events(request):
    year = datetime.now().year
    month = datetime.now().strftime('%B')
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    event_list = Event.objects.all()
    context = {
        "cal" : cal,
        "month": month,
        "year" : year,
        "event_list" : event_list,
    }
    return render(request, "com_events.html", context)

@login_required(login_url='/com_events/login/')
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            manager = request.user
            name = request.POST.get('name')
            description = request.POST.get('description')
            event = Event(name = name, manager= manager, description = description)
            event.save()
            return HttpResponseRedirect(reverse('com_events:show_events'))
    else:
        form = EventForm()
    return render(request, "forms_temp.html", {'form':form})

@login_required(login_url='/com_events/login/')
def delete(request, id):
    event = Event.objects.get(pk=id)
    event.delete()
    return redirect('com_events:show_events')

@login_required(login_url='/com_events/login/')
def join_event(request, id):
    event = Event.objects.get(pk=id)
    if request.method == 'POST':
        event.attendees.add(request.user)
        event.is_joined == True
        return redirect('com_events:show_events')
    return render(request, 'event_details.html', {'event':event})

@login_required(login_url='/com_events/login/')
def unjoin_event(request, id):
    event = Event.objects.get(pk=id)
    if request.method == 'POST':
        event.attendees.remove(request.user)
        event.is_joined == False
        return redirect('com_events:show_events')
    return render(request, 'event_details.html', {'event':event})

def register_temp(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('com_events:login')
    
    context = {'form':form}
    return render(request, 'register_temp.html', context)

def login_user_temp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("com_events:show_events")) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login_temp.html', context)

def logout_user_temp(request):
    logout(request)
    response = HttpResponseRedirect(reverse('com_events:login'))
    return response