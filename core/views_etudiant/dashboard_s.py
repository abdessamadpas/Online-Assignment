from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='access_denied_student')
def dashboard_s(request):
    user = request.user
    print("dashboard student  page user is",user)
    if user.is_staff:
        return redirect('access_denied_student')
    return render(request, 'etudiant/pages/dash_etudiant.html')