from django.shortcuts import render
from .models import book

def BookInfo(request):
    stud = book.objects.all()
    return render(request,"home.html",{'stu':stud})
