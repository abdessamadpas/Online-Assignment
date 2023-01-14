from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def profile_admin (request):
    return render(request,'admine/pages/profile_admin.html')