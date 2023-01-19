from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from core.models.auth.profile import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required()
def profile_admin (request):
    user = request.user
    print("exam page user is",user)
    if not user.is_staff:
        return redirect('access_denied_student')
    profile = Profile.objects.get(user=request.user)
    user_id=User.objects.get(username = user)
    email = user_id.email
    print(email)
    context = {
        'profile': profile ,
        'user': user_id,
        'email': email
    }
    return render(request,'admine/pages/profile_admin.html', context)