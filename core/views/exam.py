from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from core.models import Student
from core.models.group import Group
from core.models.matiere import Matiere
from core.models.question import Question
from core.models.exam import Exam
from django.template import loader

# Create your views here.
def exam (request):
    exams = Exam.objects.all().prefetch_related('question_set')
   
    template = loader.get_template('admine/pages/exam.html')
    context = { 
       'exams': exams,
    }
    return HttpResponse(template.render(context, request))
    