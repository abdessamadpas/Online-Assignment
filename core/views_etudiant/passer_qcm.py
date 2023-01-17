from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
from core.models import *

@login_required(login_url='login')
def passer_qcm(request, module_id, exam_id):
    user = request.user
    print("passer qcm   page user is",user)
    #! check if user is student or not to access this page
    print("dashboard admin  page user is",user)
    if user.is_staff:
        return redirect('access_denied_student')

    exam = get_object_or_404(Exam, id=exam_id)
    questions = Question.objects.filter(exam_id = exam.id ).prefetch_related('answer_set')
    print("questions",questions)    
    context = {
        'exam': exam,
        'module_id': module_id,
        'exam_id': exam_id,
        'questions': questions,
    }
    return render(request, 'etudiant/pages/passer_qcm.html', context)