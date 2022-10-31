import calendar
from calendar import HTMLCalendar, month_name
from datetime import datetime
from multiprocessing import context
from com_events.models import *
from com_events.forms import EventForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import *
from django.contrib import *
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers

def show_events(request):
    year = datetime.now().year
    month = datetime.now().strftime('%B')
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    context = {
        "cal" : cal,
        "month": month,
        "year" : year,
    }
    return render(request, "events_home.html", context)

def list_events(request):
    form = EventForm()
    event_list = Event.objects.all()
    context = {
        'form': form,
        'event_list':event_list
    }
    return render(request, "list_events.html", context)

@login_required(login_url='/com_events/login/')
def my_events(request):
    event_list = Event.objects.filter(attendees = request.user)
    context = {
        "event_list" : event_list,
    }
    return render(request, "my_events.html", context)


@login_required(login_url='/com_events/login/')
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            manager = request.user
            name = request.POST.get('name')
            date = request.POST.get('date')
            description = request.POST.get('description')
            event = Event(name = name, manager= manager, date=date, description = description)
            event.save()
            return HttpResponseRedirect(reverse('com_events:list_events'))
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
    event.attendees.add(request.user)
    event.is_joined == True
    return redirect('com_events:show_events')

@login_required(login_url='/com_events/login/')
def unjoin_event(request, id):
    event = Event.objects.get(pk=id)
    event.attendees.remove(request.user)
    event.is_joined == False
    return redirect('com_events:show_events')

def get_json_all(request):
    events = Event.objects.all()
    return HttpResponse(serializers.serialize('json', events), content_type='application/json')

def get_json_user(request):
    events = Event.objects.filter(attendees=request.user)
    return HttpResponse(serializers.serialize('json', events), content_type='application/json')

def add_event_ajax(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            manager = request.user
            name = data['name']
            date = data['date']
            description = data['description']
            events = Event(manager = manager, name=name, date=date, description = description)
            events.save()
        return redirect('com_events:show_events')
    return HttpResponseNotFound()