
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from core.models import *
from django.template import loader
from django.http import HttpResponse
from core.models.auth.profile import Profile
from core.views.auth.user_checks import staff_check
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.contrib.auth.models import User


@user_passes_test(staff_check, login_url='login')
def dashboard(request):

    user = request.user
    print("dashboard admin  page user is",user)
    if not user.is_staff:
        return redirect('access_denied_student')
   

    models_total = Matiere.objects.all().count()
    exams_total = Exam.objects.all().count()
    students_total = Student.objects.all().count()
    template = loader.get_template('admine/pages/index.html')
    profile = Profile.objects.get(user=request.user)
    user_id=User.objects.get(username = user)
    email = user_id.email
    context = {
        'models_total': models_total,
        'exams_total': exams_total,
        'students_total': students_total,
        'profile': profile ,
        'user': user_id,
        'email': email
    }   

    return HttpResponse(template.render(context, request))