from django.shortcuts import render
from django.shortcuts import redirect  # Import for Forms
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from .models import Image

# Import Forms
from .forms import ImageForm


# Create your views here.
def show_html(request):
    # if request.method == 'POST':
    #     form = ImageForm(request.POST, request.FILES)
    #
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Image successfully uploaded")
    #         return redirect('quotes:show_html')
    #
    # else:
    form = ImageForm()

    return render(request, 'quotes.html', {'form': form})


def get_image(request):
    images = Image.objects.all()
    return JsonResponse({"images": list(images.values())})


def add_quote(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return HttpResponse(serializers.serialize('json', [form, ]), content_type='application/json')
