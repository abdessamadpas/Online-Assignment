from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def gestion_exam (request):
    
    user = request.user
    print("gestion exam page user is",user)
    if not user.is_staff:
        return redirect('access_denied_student')
    #? your core here     
    return render(request,'admine/pages/gestion_exam.html')