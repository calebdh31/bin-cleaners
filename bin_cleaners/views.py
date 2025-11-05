from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def landing(request):
    if request.user.is_authenticated:
        return redirect('user_bookings')
    return render(request, 'landing.html')