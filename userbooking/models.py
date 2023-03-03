from django.db import models

# Create your models here.
class booking(models.Model):
    Contact = models.CharField(max_length=20)
    Reason = models.CharField(max_length=200)
    Council = models.CharField(max_length=100)
    Room = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=100,default="awaiting")

