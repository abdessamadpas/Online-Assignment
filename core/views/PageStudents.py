from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def PageStudents (request):
    return render(request,'admin/studentSection.html')
