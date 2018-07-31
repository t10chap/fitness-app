from django.shortcuts import render

# from .models import User
# from .models import User, Custom_Meals, Custom_Circuit
# from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from pprint import pprint


def landing(request):
    return render(request, "fitness_app/landing.html", {})


def index(request):
    return render(request, "fitness_app/index.html", {})


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "fitness_app/profile.html", {"username": username})


############## LOG IN ############

# root page
def login_view(request):
    if request.method == "POST":
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/index")
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, "fitness_app/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        # if post, then authenticate (user submitted username and password)
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/index")
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = SignupForm()
        return render(request, 'fitness_app/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/index")


############# HOMEPAGE ###########

# homepage


def homepage(request):
    return render(request, "fitness_app/homepage.html")


############# PROFILE ###########

# profile


def dashboard(request, username):
    return render(request, 'fitness_app/dashboard.html')


################ WORKOUT API ############

# GET

def find_workout(request):
    url = 'https://wger.de/api/v2/exercise/'
    r = requests.get(url=url)
    r
    r.content
    return HttpResponse(r)

################ FOOD API ############

def find_food(request):
    r = requests.get("https://wger.de/api/v2/exercise/?limit=1")
    r.content


