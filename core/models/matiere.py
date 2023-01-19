from django.db import models
from core.models.group import Group
from django.contrib.auth.models import User

class Matiere(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=300,null=True)
    groupe = models.ForeignKey(Group, on_delete=models.CASCADE,null=True)
    
    #questions = models.ManyToManyField(Question)



    def __str__(self) :
        return self.name
