from django.shortcuts import render

from core.models.exam import Exam
# Create your views here.


def afficher_qcm(request):
    exams_extracted = Exam.objects.all()
    print(exams_extracted)
    context = {
        'exams': exams_extracted
    }
    return render(request, 'etudiant/pages/afficher_qcm.html', context)