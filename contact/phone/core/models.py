from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null = True, blank = True)
    number = models.CharField(max_length=13, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return self.name + ' | ' + str(self.author) + '  |  ' + str(self.date_added)