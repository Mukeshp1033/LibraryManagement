from django.contrib import admin
from .models import book

#admin.site.register(book)

class adminbook(admin.ModelAdmin):
    list_display= ["Book_Name","Subject","Author_Name"]

admin.site.register(book,adminbook)