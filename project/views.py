from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#from . import forms
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username').lower()
            password = request.POST.get('password')
            
            try:
                user= User.objects.get(username=username)
            except:
                messages.error(request, 'Username does not exists!') 
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password does not exists')
        return render(request,"log_in.html")

def log_out(request):
     logout(request)
     return redirect('index1')
 
@login_required(login_url='/login')
def home(request):
    
     return render(request, 'home.html')
def index(request):
    return render(request, "index.html")

@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            f = CustomUserCreationForm(request.POST)
            if f.is_valid():
                f.save()
                user = f.cleaned_data.get('username')
                messages.success(request, 'Account was successfully created for ' + user)
                return redirect('home')

        else:
            f = CustomUserCreationForm()
            
        return render(request, 'signup.html', {'form': f})


def about(request):
    
    return render(request, "about.html")
# Create your views here.
