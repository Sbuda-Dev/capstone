from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
''' The following functions will allow a user to be registered. The registered 
user will then be able to login and view the contents of the webpage, which is
an online museum.'''

def user_login(request):

   

    return render(request, 'authentication/login.html')

def authenticate_user(request):

    ''' This function will authenticate the user's username and password. If 
    these are correct, they will be able to view the contents of the webpage.'''

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)

    if user is None:

        return HttpResponseRedirect(reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
    
def show_user(request):

    ''' This function will allow the user to view their username and password.'''

    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register_view(request):

    ''' This function will allow the user to register another if their credentials
    are noton the fatabase already.'''

    if request.method == "POST":
        form = UserCreationForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        else:
            form = UserCreationForm()

    return render(request, "authentication/register.html",
            {"form": form})

def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            return redirect("posts:list")

    else:
        form = AuthenticationForm()

    return render(request, "authentication/login.html", {"form": form})
