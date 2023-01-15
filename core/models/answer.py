from django.db import models

class Answer(models.Model):
    answer = models.CharField(max_length=50, null=True)
    question_id = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self) :
        return self.answer
