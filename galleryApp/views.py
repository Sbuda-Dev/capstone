from django.shortcuts import render 
from .models import Exhibit
from django.http import HttpResponse 


def exhibit_list(request): 
	exhibits = Exhibit.objects.all() 
	return render(request, 'index.html', {'exhibits': exhibits}) 


def home(request): 
	return HttpResponse('Hello, World!') 
