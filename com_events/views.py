import calendar
from calendar import HTMLCalendar, month_name
from datetime import datetime
from com_events.models import *
from com_events.forms import EventForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

def show_events(request):
    return render(request, "events_home.html")

def list_events(request):
    form = EventForm()
    event_list = Event.objects.all()
    context = {
        'form': form,
        'event_list':event_list
    }
    return render(request, "list_events.html", context)

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
    event.save()
    return redirect('com_events:show_events')

@login_required(login_url='/com_events/login/')
def unjoin_event(request, id):
    event = Event.objects.get(pk=id)
    event.attendees.remove(request.user)
    event.is_joined == False
    event.save()
    return redirect('com_events:show_events')

def get_json_all_mobile(request):
    events = Event.objects.all()
    data = [{
                'model':'com_events.event',
                'pk': event.pk,
                'fields':{
                    'name':event.name,
                    'date':event.date,
                    'description':event.description,
                    'is_joined':event.is_joined,
                    'attendees':[attendee.username for attendee in event.attendees.all()],
                }
            }for event in events]
    return JsonResponse(data, safe=False)

def get_json_all(request):
    events = Event.objects.all()
    return JsonResponse({
        'data':
            [{
                'model':'com_events.event',
                'pk': event.pk,
                'fields':{
                    'name':event.name,
                    'date':event.date,
                    'description':event.description,
                    'is_joined':event.is_joined,
                    'attendees':[attendee.username for attendee in event.attendees.all()],
                }
            }for event in events]
    })

def get_json_user(request):
    events = Event.objects.filter(attendees=request.user)
    return JsonResponse({
        'data':
            [{
                'model':'com_events.event',
                'pk': event.pk,
                'fields':{
                    'name':event.name,
                    'date':event.date,
                    'description':event.description,
                    'is_joined':event.is_joined,
                    'attendees':[attendee.username for attendee in event.attendees.all()],
                }
            }for event in events]
    })

@login_required(login_url='/com_events/login/')
def add_event_ajax(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            date = data['date']
            description = data['description']
            events = Event(name=name, date=date, description = description)
            events.save()
        return redirect('com_events:show_events')
    return HttpResponseNotFound()

@csrf_exempt
def add_event_flutter(request):
    if request.method == 'POST':
        form = json.loads(request.POST)
        name = form.get('name')
        date = form.get('date')
        description = form.get('description')
        events = Event(name=name, date=date, description = description)
        events.save()
        return JsonResponse({"message":"Berhasil mengupload!"})
