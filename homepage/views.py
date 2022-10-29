from django.shortcuts import render

def show_homepage(request):
    return render(request, 'homepage.html')


def register_temp(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('com_events:login')

    context = {'form': form}
    return render(request, 'register_temp.html', context)


def login_user_temp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("com_events:show_events"))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login_temp.html', context)


def logout_user_temp(request):
    logout(request)
    response = HttpResponseRedirect(reverse('com_events:login'))
    return response