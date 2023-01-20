from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from core.models.auth.profile import Profile
from core.models import *
from core.models.exam import Exam
# Create your views here.

@login_required(login_url='login')
def afficher_qcm(request):
    user = request.user
    print("afficher qcm page user is",user)
    if user.is_staff:
        return redirect('access_denied_student')
    groupe_student = Student.objects.get(user=user).group_id
    exams_extracted = Exam.objects.filter(group_id=groupe_student).prefetch_related('attempter_set')
    
    for exam in exams_extracted:
        print("Exam: ", exam)
        print("Attempters: ", exam.attempter_set.count())
    
    #attempter_exam = Attempter.objects.filter(exam=user)
    
    profile = Profile.objects.get(user=user)
    context = {
        'exams': exams_extracted,
        'profile': profile
    }
    return render(request, 'etudiant/pages/afficher_qcm.html', context)
