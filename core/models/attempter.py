from django.db import models
from django.contrib.auth.models import User
from core.models import *
#3rd apps field


class Attempter(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	score = models.PositiveIntegerField()
	completed = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username