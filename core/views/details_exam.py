from django.template import loader
from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Exam
from core.models.answer import Answer
from core.models.question import Question
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def details_exam(request):
    exam_id = request.GET.get('exam_id')
    exam = Exam.objects.get(id=exam_id)
    questions = Question.objects.filter(exam_id=exam_id).prefetch_related('answer_set')
    template = loader.get_template('admine/pages/details_exam.html')
    context = {
        'questions': questions,
        'exam': exam
    }
    return HttpResponse(template.render(context, request))