from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from hello.forms import NewUserForm
from hello.models import Greeting, Tutorial

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "main/about.html")

def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"tutorials":Tutorial.objects.all})

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index.html")

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

def register(request):
    # form = UserCreationForm
    # return render(request = request,
    #               template_name = "main/register.html",
    #               context={"form":form})
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def allbuilding(request):
    return render(request, "building/all-building.html")

def newmanlibrary(request):
    return render(request, "building/newman-library.html")

def togressonhall(request):
    return render(request, "building/togresson-hall.html")

def mcbrydehall(request):
    return render(request, "building/mcbryde-hall.html")