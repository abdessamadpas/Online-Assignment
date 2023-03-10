
from django.shortcuts import render,redirect

from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from core.models.auth.profile import Profile
from django.contrib.auth.decorators import login_required
from core.models.exam import Exam
# Create your views here.
@login_required()
def gestion_exam (request):
    
    user = request.user
    print("gestion exam page user is",user)
    if not user.is_staff:
        return redirect('access_denied_student')
    #? your core here
    exams_extracted = Exam.objects.all()
    print(exams_extracted)
    profile = Profile.objects.get(user=request.user)
    user_id= User.objects.get(username = user)
    email = user_id.email    
    context = {
        'profile': profile ,
        'user': user_id,
        'email': email,
        'exams':exams_extracted
    } 
    return render(request,'admine/pages/gestion_exam.html', context)