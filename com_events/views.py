from django.urls import reverse
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar, month_name
from datetime import datetime
from com_events.models import *
from com_events.forms import EventForm
from django.http import HttpResponseRedirect

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

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('com_events:show_events'))
    else:
        form = EventForm()
    return render(request, "forms_temp.html", {'form':form})

def delete(request, id):
    event = Event.objects.get(pk=id)
    event.delete()
    return redirect('com_events:show_events')

def join_event(request, id):
    event = Event.objects.get(pk=id)
    if request.method == 'POST':
        event.attendees.add(request.user)
        return redirect('com_events:show_events')
    return render(request, 'event_details.html', {'event':event})