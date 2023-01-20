from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from core.models import *
from core.models.auth.profile import Profile
# Create your views here.

@login_required(login_url='login')
def resultat_qcm(request):
    user = request.user
    if user.is_staff:
        return redirect('access_denied_student')
    results = Attempter.objects.filter(user=user).order_by('-create_at')
    print("result number is ",results.count())
    if results.count() == 0:
        return render(request, 'etudiant/pages/resultat_qcm.html')
    
    
    
    context = {
        "results": results,
        

    }

   
    return render(request, 'etudiant/pages/resultat_qcm.html', context)