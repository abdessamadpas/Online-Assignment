from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.template import loader
from django.http import HttpResponse
from core.models import Student
from core.forms.student import StudentForm

# Create your views here.
def student (request):

    students = Student.objects.all()
    template = loader.get_template('admine/pages/student.html')

    context = {
        'students': students,
    }

    return HttpResponse(template.render(context, request))