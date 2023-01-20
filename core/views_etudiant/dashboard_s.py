from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import *
from core.models import matiere
# Create your views here.


@login_required(login_url='access_denied_student')
def dashboard_s(request):
    user_id = request.user
    print("dashboard student page user is",user_id)
    if user_id.is_staff:
        return redirect('access_denied_student')

    profile = Profile.objects.get(user=user_id)
    groupe_id = Student.objects.get(user=user_id).group_id.id
    print("ccccccc",groupe_id)
    modeles_total = Matiere.objects.filter(groupe=groupe_id).count()
    print("matiere totale is",matiere)
    examen_total = Exam.objects.filter(group_id=groupe_id).count()
    # matiere_user = Matiere.objects.all()
    # print("matiere_user",matiere_user)

    # modeles_total = matiere_user.count()
    # examen_total = Exam.objects.filter(groupe=groupe_objet.id).count()
    
    # group = Matiere.objects.filter(groupe=student.groupe)

    context={
        'profile': profile,
         'modeles_total': modeles_total,
         'examen_total': examen_total,

    }
    return render(request, 'etudiant/pages/dash_etudiant.html', context)
