from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
import json
from django.views.generic import View

class StudentDetails(View):
    def get(self,request,id,*args, **kwargs):
        stu = Student.objects.get(id = id)
        stu_data = {'no':stu.no,'name':stu.name,'marks':stu.marks,'addr':stu.addr}
        json_data = json.dumps(stu_data)
        return HttpResponse(json_data,content_type = 'application/json')