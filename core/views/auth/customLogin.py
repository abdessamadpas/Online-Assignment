from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
class RoleBasedLoginView(LoginView):
    template_name = 'admine/pages/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        print(user, user.is_staff)
        if user.is_staff:
            print(redirect('dashboarde' ))
            print(reverse_lazy('dashboarde'))

            return redirect('dashboarde')
        else:
            print(redirect('dashboard_s'))

            return redirect('dashboard_s')
