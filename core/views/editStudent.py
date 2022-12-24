from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def editStudent (request):
    return render(request,'admine/dashboard.html')
