from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def profile_admin (request):
    user = request.user
    print("exam page user is",user)
    if not user.is_staff:
        return redirect('access_denied_student')
    return render(request,'admine/pages/profile_admin.html')