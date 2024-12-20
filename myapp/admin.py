from django.contrib import admin
from myapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    i = ['name','id','marks','addr']
admin.site.register(Student,StudentAdmin)