from django.db import models

class Note(models.Model):

    exam_id = models.ForeignKey('Exam', on_delete=models.CASCADE )
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE )
    note = models.PositiveIntegerField(default=0)
    
    

    def __str__(self) :
       return str(self.note)