from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# when we update our form fields in forms.py we wil import that form instead of usercreationform and use that class
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(
            tutorial_category__category_slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(
                tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug
        return render(request, "main/category.html", {"part_ones": series_urls})
    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.filter(tutorial_slug=single_slug)
        # tutorials_from_series = Tutorial.objects.filter(
        #     tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("tutorial_published")

        return render(request, "main/tutorial.html", {'tutorials': this_tutorial})
    return HttpResponse(f"{single_slug} does not correspond to anything")


def home(request):
    return render(request, 'main/categories.html', {"categories": TutorialCategory.objects.all})


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
