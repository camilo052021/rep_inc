from django.shortcuts import render, redirect
from .forms import UserRegisterForm


# Create your views here.
def home(request):
    return render(request, 'newsfeed.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)
