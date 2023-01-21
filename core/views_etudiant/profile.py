from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models.auth.profile import Profile
from core.models.student import Student
# Create your views here.

@login_required(login_url='login')
def profile(request):
    user = request.user
    print("dashboard admin  page user is",user)
    if user.is_staff:
        return redirect('access_denied_student')
    
    profile = Profile.objects.get(user=request.user)
    student = Student.objects.get(user=request.user)
    grad_stud = student.grade



    context = {
        'user': user.id,
        'profile': profile,
        'student': student,
        'grade': grad_stud
    }

    return render(request, 'etudiant/pages/profile.html', context)