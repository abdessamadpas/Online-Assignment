from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def edit_exam(request):
    user=request.user
    print("gestion exam page user is",user)
    #?if not user.is_stuff:
        #?return redirect('access_denied_student')
    return render(request, 'admine/pages/edit_exam.html')