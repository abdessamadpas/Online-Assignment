from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from core.models import *
# Create your views here.

@login_required(login_url='login')
def resultat_qcm(request):
    user = request.user
    print("dashboard admin  page user is",user)
    if user.is_staff:
        return redirect('access_denied_student')
    results = Attempter.objects.filter(user=user).order_by('-create_at')
    exam_name = Attempter.objects.filter(user=user).first().exam
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