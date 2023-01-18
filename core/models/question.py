from django.db import models



class Question(models.Model):
    question = models.CharField(max_length=50, null=True)
    exam_id = models.ForeignKey('Exam', on_delete=models.SET_NULL, null=True)
    points = models.PositiveIntegerField(default=1)
    
    
    def __str__(self) :
        return self.question