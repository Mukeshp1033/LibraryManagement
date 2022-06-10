
from django.db import models

class book(models.Model):
    Book_Name= models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Author_Name = models.CharField(max_length=100)
    Availble_status= models.BooleanField(default=False)

