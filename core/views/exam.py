from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def exam (request):
    return render(request,'admine/pages/exam.html')