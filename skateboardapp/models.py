from django.db import models

# Create your models here.
class Skateboard(models.Model):
    id = models.AutoField(primary_key=True)
    available = models.BooleanField()
    owner = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    weight = models.IntegerField()
    length = models.IntegerField()
    type = models.CharField(max_length=20) #skateboard, longboard,pennyboard
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
