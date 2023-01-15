from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def EditModels (request):
    return render(request,'admine/dashboard.html')
