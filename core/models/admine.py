from django.db import models

# Create your models here.
class Admine(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True )
    password = models.CharField(max_length=50, null=True )
    image = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self) :
        return self.name