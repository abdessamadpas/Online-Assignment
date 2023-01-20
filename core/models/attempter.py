from django.db import models
from django.contrib.auth.models import User
from core.models import *
from django.utils import timezone
#3rd apps field

COMPLATED = (
	('completed', 'completed'),
	('not completed', 'not completed'),
)
class Attempter(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	score = models.PositiveIntegerField()
	completed = models.CharField(max_length=1000, choices=COMPLATED, default='completed')
	create_at = models.DateTimeField(default=timezone.now)
	module = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.user.username