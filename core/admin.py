from django.contrib import admin

# Register your models here.

from core.models import * 

admin.site.register(Admine)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Matiere)
admin.site.register(Student)


