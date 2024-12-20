from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=30)
    no = models.CharField(max_length=30)
    marks = models.FloatField(max_length=30)
    addr = models.CharField(max_length=30)

    