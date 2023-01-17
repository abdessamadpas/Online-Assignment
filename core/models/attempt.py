from django.db import models
from core.models import *
class Attempt(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	attempter = models.ForeignKey(Attempter, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
