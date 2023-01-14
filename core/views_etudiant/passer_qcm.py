from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def passer_qcm(request):
    return render(request, 'etudiant/pages/passer_qcm.html')