from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def gestion_exam (request):
    return render(request,'admine/pages/gestion_exam.html')