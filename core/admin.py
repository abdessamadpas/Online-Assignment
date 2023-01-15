from django.contrib import admin

# Register your models here.

from core.models import * 
from core.models.auth.models import *
class students_display(admin.ModelAdmin):

    list_filter= ('name', 'email', 'group_id')
    list_display = ('name','email','group_id')

class examens_display(admin.ModelAdmin):

    list_filter= ('name', 'duration', 'group_id','matier_id')
    list_display = ('name','duration','group_id','matier_id')

admin.site.register(Admine)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Matiere)
admin.site.register(Student, students_display)
admin.site.register(Profile)
admin.site.register(Exam)
admin.site.register(Group)
admin.site.register(Note)



