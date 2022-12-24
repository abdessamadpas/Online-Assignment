from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def getModels (request):
    return render(request,'admine/studentSection.html')
