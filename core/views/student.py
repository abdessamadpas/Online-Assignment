from django.shortcuts import render, redirect


from django.http import HttpRequest,HttpResponse
from django.template import loader
from django.http import HttpResponse
from core.models import Student
from core.models.group import Group
from core.models.matiere import Matiere
from core.forms.student import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models.auth.profile import Profile

# Create your views here.
@login_required()
def student (request):
    user = request.user
    print("helooooooooo",user)
    if not user.is_staff:
        return redirect('access_denied_student')
    students = Student.objects.all()
    groups = Group.objects.all()
    matieres = Matiere.objects.all()
    profile = Profile.objects.get(user=request.user)
    user_id=User.objects.get(username = user)
    email = user_id.email
    template = loader.get_template('admine/pages/student.html')
    
    context = {
        'students': students,
        'options_list_groups': groups,
        'options_list_matieres': matieres,
        'profile': profile ,
        'user': user_id,
        'email': email
    }

    return HttpResponse(template.render(context, request))