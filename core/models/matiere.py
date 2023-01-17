from django.db import models
from django.contrib.auth.models import User

class Matiere(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=300,null=True)
    enrolled = models.ManyToManyField(User)
    #questions = models.ManyToManyField(Question)



    def __str__(self) :
        return self.name
