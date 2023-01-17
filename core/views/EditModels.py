from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
def EditModels (request):
    user=request.user
    if not user.is_stuff :
        return redirect('access_denied_student')
    return render(request,'admine/dashboard.html')
