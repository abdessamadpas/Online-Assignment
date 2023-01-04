from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def student (request):
    return render(request,'admine/pages/student.html')
