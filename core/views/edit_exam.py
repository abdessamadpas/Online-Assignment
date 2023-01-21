from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from core.models.exam import Exam
from core.models.question import Question
from django.http import HttpResponse
# Create your views here.
@login_required()
def edit_exam(request):
    user=request.user
    print("gestion exam page user is",user)
    #?if not user.is_stuff:
        #?return redirect('access_denied_student')
    exam_id = request.GET.get('exam_id')
    print("exam_id",exam_id)
    exam = Exam.objects.get(id=exam_id)
    questions = Question.objects.filter(exam_id=exam_id).prefetch_related('answer_set')
    template = loader.get_template('admine/pages/edit_exam.html')
    context = {
        'questions': questions,
        'exam': exam
    }
    return HttpResponse(template.render(context, request))   