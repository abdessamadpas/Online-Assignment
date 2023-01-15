from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    group_id = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)
   
    
    def __str__(self) :
        return self.name
