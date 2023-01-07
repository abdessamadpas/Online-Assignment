from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def gestion_exam (request):
    return render(request,'admine/pages/gestion_exam.html')