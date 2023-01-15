from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile_admin (request):
    return render(request,'admine/pages/profile_admin.html')