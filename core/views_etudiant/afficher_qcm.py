from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def afficher_qcm(request):
    return render(request, 'etudiant/pages/afficher_qcm.html')