from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def edit_exam(request):
    return render(request, 'admine/pages/edit_exam.html')