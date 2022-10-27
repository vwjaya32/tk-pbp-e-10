from django.shortcuts import render
from django.shortcuts import redirect
from mh_tests.models import *
# Create your views here.

def mhtestpage(request):
    mh_list = MentalTest.objects.all()
    context = {
        'data': mh_list,
    }
    return render(request, "mhtest.html", context)