from django.shortcuts import render
from django.shortcuts import redirect  # Import for Forms
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import Image

# Import Forms
from .forms import ImageForm


# Create your views here.
def show_html(request):
    data = Image.objects.all()
    form = ImageForm()
    user = request.user
    context = {
        'images': data,
        'form': form,
        'user': user,
    }
    return render(request, 'quotes.html', context)


def get_image(request):
    images = Image.objects.all().order_by('pk')
    return JsonResponse({"images": list(images.values())})


def delete_image(request, id):
    image = Image.objects.get(pk=id)
    image.delete()
    messages.success(request, "Image has been deleted")
    return redirect('quotes:show_html')

@login_required(login_url='/homepage/login/')
def add_quote(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)

        if form.is_valid():
            data      = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, "Image successfully uploaded")
            return redirect('quotes:show_html')

    else:
        form = ImageForm()

    return render(request, 'add_quote.html', {'form': form})


def ajax_add_quote(request):
    return
    # if request.method == 'POST':
    #     form = ImageForm(request.POST, request.FILES)
    #
    #     if form.is_valid():
    #         form.save()
    #     return HttpResponse(serializers.serialize('json', [form, ]), content_type='application/json')
