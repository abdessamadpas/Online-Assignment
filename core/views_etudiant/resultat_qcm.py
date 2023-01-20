from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from core.models import *
from core.models.auth.profile import Profile
# Create your views here.

@login_required(login_url='login')
def resultat_qcm(request):
    user = request.user
    print("dashboard admin  page user is",user)
    if user.is_staff:
        return redirect('access_denied_student')
    results = Attempter.objects.filter(user=user).order_by('-create_at')
    print("results",results)
    exam_name = Attempter.objects.filter(user=user).first().exam
    print("exam_name",exam_name)
    exam_id=exam_name.id
    exam_selected = Exam.objects.get(id=exam_id)
    matiere_id = exam_selected.matiere_id.id
    matiere = Matiere.objects.get(id=matiere_id).name
    print("matiere",matiere)
    context = {
        "results": results,
        "matiere": matiere,
        "exam": exam_name,
        "user": user,

    }

   
    return render(request, 'etudiant/pages/resultat_qcm.html', context)