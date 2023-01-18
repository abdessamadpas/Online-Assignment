from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models.auth.profile import Profile
# Create your views here.


@login_required(login_url='access_denied_student')
def dashboard_s(request):
    user_id = request.user
    print("dashboard student  page user is",user_id)
    if user_id.is_staff:
        return redirect('access_denied_student')
    profile = Profile.objects.get(user=user_id)
    context={
        'profile': profile
    }
    return render(request, 'etudiant/pages/dash_etudiant.html', context)
