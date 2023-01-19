from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.models.exam import Exam
# Create your views here.

@login_required(login_url='login')
def afficher_qcm(request):
    user = request.user
    print("afficher qcm page     user is",user)
    if user.is_staff:
        return redirect('access_denied_student')
    exams_extracted = Exam.objects.all()
    print(exams_extracted)
    context = {
        'exams': exams_extracted
    }
    return render(request, 'etudiant/pages/afficher_qcm.html', context)