from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def settings (request):
    user=request.user
    if not user.is_stuff :
        return redirect('access_denied_student')
    return render(request,'admine/dashboard.html')
