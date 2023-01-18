from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from core.models.auth.profile import Profile
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
    profile = Profile.objects.get(user=user)
    context = {
        'exams': exams_extracted,
        'profile': profile
    }
    return render(request, 'etudiant/pages/afficher_qcm.html', context)