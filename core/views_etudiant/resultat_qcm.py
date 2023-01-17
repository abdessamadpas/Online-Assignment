from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def resultat_qcm(request):
    user = request.user
    print("dashboard admin  page user is",user)
    if user.is_staff:
        return redirect('access_denied_student')
    return render(request, 'etudiant/pages/resultat_qcm.html')