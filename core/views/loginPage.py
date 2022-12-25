from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from core.forms import LoginForm
from django.http import HttpResponseRedirect

# Create your views here.
def loginPage (request):
    
    return render(request,'admine/login.html')