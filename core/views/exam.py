from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from core.models import Student
from core.models.group import Group
from core.models.matiere import Matiere
from core.models.question import Question
from core.models.exam import Exam
from django.template import loader
from django.contrib.auth.models import User
from core.models.auth.profile import Profile

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def exam (request):

   user = request.user
   print("profile page user is",user)
   if not user.is_staff:
      return redirect('access_denied_student')

   exams = Exam.objects.all().prefetch_related('question_set')
   profile = Profile.objects.get(user=request.user)
   user_id=User.objects.get(username = user)
   email = user_id.email
   template = loader.get_template('admine/pages/exam.html')
   context = { 
       'exams': exams,
       'profile': profile ,
       'user': user_id,
       'email': email
    }
   return HttpResponse(template.render(context, request))
    