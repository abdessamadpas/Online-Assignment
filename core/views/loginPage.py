from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from core.forms import LoginForm
from django.http import HttpResponseRedirect

# Create your views here.
def loginPage (request):
    if request.method == 'POST' :
        print("checking")
        form = LoginForm(request.POST)

        if form.is_valid():
            print("passed valid")

            # process the data in form.cleaned_data as required
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username,password)

            # redirect to a new URL:

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Redirect to a success page.
                redirect('dashboard')
                
            else:
                # Return an 'invalid login' error message.
                pass
    else:
        form = LoginForm()
    return render(request,'admin/login.html', {'form': form})