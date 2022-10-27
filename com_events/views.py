import datetime
from typing import List
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar, month_name
from datetime import datetime

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
    return render(request, "com_events.html", context)
