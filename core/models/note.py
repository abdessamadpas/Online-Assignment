from django.db import models

class Note(models.Model):

    exam_id = models.ForeignKey('Exam', on_delete=models.CASCADE )
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE )
    
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    
    

    def __str__(self) :
        return self.name
