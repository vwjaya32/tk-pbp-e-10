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
    form = ImageForm()

    context = {
        'form': form,
    }
    return render(request, 'quotes.html', context)


def get_image(request):
    images = Image.objects.all().order_by('-pk')
    # User who run this command
    user = request.user

    # Admin status
    admin_stat = True if user.is_superuser else False

    return JsonResponse({
        'data':
            [{
                'model': 'quotes.image',
                'pk': image.id,
                'who': user.username,
                'admin_stat': admin_stat,
                'fields': {
                    'title': image.title,
                    'image': image.image,
                    'user': image.user.username,
                }
            } for image in images]
    })


@login_required(login_url='/home/login/')
def delete_image(request, id):
    image = Image.objects.get(pk=id)
    image.delete()
    messages.success(request, "Image has been deleted")
    return redirect('quotes:show_html')


@login_required(login_url='/home/login/')
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


@login_required(login_url='/home/login/')
def ajax_add_quote(request):
    if request.method == "POST":
        form = ImageForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user  = request.user
            title = data['title']
            image = data['image']
            new_image = Image(user=user, title=title, image=image)
            new_image.save()
            return HttpResponse(200)
    return HttpResponse(404)

