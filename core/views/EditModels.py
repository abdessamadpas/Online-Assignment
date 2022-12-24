from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


def EditModels (request):
    return render(request,'admine/dashboard.html')
