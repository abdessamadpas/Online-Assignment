from django.db import models
from django.contrib.auth.models import User



class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=50, null=True)
    exam_id = models.ForeignKey('Exam', on_delete=models.SET_NULL, null=True)
    points = models.PositiveIntegerField(default=1)
    
    def __str__(self) :
        return self.question