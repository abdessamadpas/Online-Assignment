from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def resultat_qcm(request):
    return render(request, 'etudiant/pages/resultat_qcm.html')