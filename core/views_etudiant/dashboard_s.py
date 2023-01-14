from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard_s(request):
    return render(request, 'etudiant/pages/dash_etudiant.html')