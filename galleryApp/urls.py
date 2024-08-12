from django.urls import path 
from . import views 

urlpatterns = [ 
	path('home/', views.home, name='home'), 
	path('', views.exhibit_list, name='exhibit_list'), 
] 
