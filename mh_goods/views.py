from django.shortcuts import render
from django.shortcuts import redirect
from mh_goods.models import *
# Create your views here.

def mhgoods(request):
    # if request.user.is_authenticated:
    #     mh_list = MentalTest.objects.filter(user=request.user)
    #     context = {
    #         'data': mh_list,
    #     }
    #     return render(request, "mhtest.html", context)
    # else:
        return render(request, "mhgoods.html")
