from django.shortcuts import render
from django.shortcuts import redirect
from mh_tests.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.
# def username_in(request):
#     username = None
#     if request.user.is_authenticated:
#         username = request.user.username
#         return username

@login_required(login_url='/homepage/login/')
def mhtestpage(request):
    mh_list = MentalTest.objects.filter(user=request.user)
    context = {
        'data': mh_list,
    }
    return render(request, "mhtest.html", context)
    
@login_required(login_url='/homepage/login/')
def save_points(request):
    if request.method == 'POST':
        user = request.user
        score = request.POST.get("score")
        date = request.POST.get("date")
        new_result = MentalTest( user=user, score=score, date=date)
        new_result.save()

        return JsonResponse(
            {"pk" : new_result.pk, 
            "fields": {
            "user" : model_to_dict(new_result.user),
            "score" : new_result.score,
            "date" : new_result.date,
        }})
    return HttpResponseNotFound()

def json_res(request):
    data = MentalTest.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/homepage/login/')
@csrf_exempt
def delete_res(request, pk):
    lists=MentalTest.objects.get(id=pk)
    lists.delete()
    messages.success(request, "Your result has been deleted.")
    return redirect ('mh_tests:mhtest')