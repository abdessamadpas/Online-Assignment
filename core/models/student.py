from django.db import models
from django.contrib.auth.models import User

GRADES=(
    ('1CP','1CP'),
    ('2CP','2CP'),
    ('3IIR','3IIR'),
    ('4IIR','4IIR'),
)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student',null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    group_id = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=50, null=True, choices=GRADES)

    
    def __str__(self) :
        return self.name
