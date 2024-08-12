from django.db import models 

class Exhibit(models.Model): 
	name = models.CharField(max_length=255) 
	description = models.TextField() 
	image = models.ImageField(upload_to='exhibits/') 
	created_at = models.DateTimeField(auto_now_add=True) 
	updated_at = models.DateTimeField(auto_now=True) 

	def __str__(self): 
		return self.name 
