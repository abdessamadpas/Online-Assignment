from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def profile(request):
    return render(request, 'etudiant/pages/profile.html')