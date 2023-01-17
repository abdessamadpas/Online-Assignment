from django.db import models
from datetime import datetime


class Exam(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000, null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    expiration_date = models.DateField(default=datetime.now  )
    duration = models.CharField(max_length=50, null=True )
    allowed_attempts = models.PositiveIntegerField(default=1)
    group_id = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)
    matiere_id = models.ForeignKey('Matiere', on_delete=models.SET_NULL, null=True)
    
    
    #Questions = models.ManyToManyField('Question', blank=True)



    def __str__(self) :
        return self.title
