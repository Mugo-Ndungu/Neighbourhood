from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighbour(models.Model):
    user = models.ForeignKey(User,null=False)
    name = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='Neighbour/',null=True)
    occupants = models.IntegerField(null=False)
    police = models.IntegerField(default='eg 999,269')
    hospital = models.IntegerField(null=True)
    objects=models.Manager()

    def __str__(self):
        return self.name