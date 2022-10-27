from django.shortcuts import render

def show_events(request):
    return render(request, "com_events.html")
