from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# when we update our form fields in forms.py we wil import that form instead of usercreationform and use that class
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'main/home.html', {"tutorials": Tutorial.objects.all()})


def register(request):
    if(request.method == 'POST'):
        form = NewUserForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account created : {username}")
            login(request, user)
            return redirect("/")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = NewUserForm
    return render(request, 'main/register.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully")
    return redirect('/')


def login_request(request):
    if(request.method == "POST"):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if(user is not None):
                messages.success(request, f"Welcome! {username}")
                login(request, user)
                return redirect("/")
            else:
                for msg in form.error_messages:
                    messages.error(
                        request, f"{msg}:{form.error_messages[msg]}")
        else:
            for msg in form.error_messages:
                messages.error(
                    request, f"{msg}:{form.error_messages[msg]}")

    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})
