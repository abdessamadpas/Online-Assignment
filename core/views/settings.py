from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def settings (request):
    return render(request,'admine/dashboard.html')
