from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def details_exam(request):
    return render(request, 'admine/pages/details_exam.html')