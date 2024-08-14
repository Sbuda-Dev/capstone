"# capstone" 
The 'gallery' program

Table of contents:

I. About program
II. Setting up your virtual environment
III. Installing Django
IV. Setting up urls 


I. This is a program where a user can view an online gallery (museum).
The user will have to create a username and password using Django.
Once their credentials have been added and authenticated, the user will
be able to view the exhibits on the webpage.
There is a requirements lists that comes with the program which will assist
the user with installing all the necessary programs.

II. Setting up a virtual environment. Use a terminal to 'cd' to your project directory.
Once there, run the command 'python -m env [your virtual environment name]'. To activate
your virtual environment, cd to the Scripts folder and run the command '.\Activate'.
Now that your VE has been activated, you can now install Django by running the following
command: python -m pip install django or pip install django.

III. Once Django has been installed, use the command "django-admin startproject [your projecct name]"
to start your project. In your terminal, while the virtual environment is still active, run the command:
python manage.py runserver, to see if the project was created successfully. It will lead you to the default 
local host port 8000.Next you will run the "python manage.py startapp [your app name]" command
to create a Django app. 

IV. In your project folder, in the settings file, under 'INSTALLED_APPS', enter
your app's name in single-inverted commas ('app name',). Go to the views.py file and add the output function, i.e,
'def index (request):
  return HttpResponse("Hello, world. You're at the polls index.")'
This you modify after having veried that everything works correctly. Still in your project folder, create a 'urls.py' file,
then insert the following lines in it:

from django.urls import path

from . import views

urlpatterns = [
path(" ", views.index, name="index"),
]
In the terminal, run the command "python manage.py runserver", if it runs successfully, you're ready to modify the project
into the 'exhibit/gallery' project.

V. First create a Docker account (in the DockerHub website) and sign in. In your IDE terminal, first run the command
'docker login', if the login is successful, run the command 'docker run hello-world'. In your project folder, create a folder,
give it any name, cd into that folder then in your IDE create a dockerfile (no extensions) and add the lines:

FROM python:3.10-slim-buster
WORKDIR /capstone
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

Once the project is running, you'll be able to set up the html for the exhibit webpage.
If you get stuck, you can refer to the "Pictures" folder.



