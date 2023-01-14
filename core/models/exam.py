from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    duration = models.CharField(max_length=50, null=True )
    group_id = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)
    matiere_id = models.ForeignKey('Matiere', on_delete=models.SET_NULL, null=True)
    #Questions = models.ManyToManyField('Question', blank=True)



    def __str__(self) :
        return self.name
