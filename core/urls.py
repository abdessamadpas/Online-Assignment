from django.urls import path
from core import views , views_etudiant
from django.shortcuts import redirect


urlpatterns = [

    path('', views.dashboard , name='dashboard'),
    path('login/', views.loginPage, name='login' ),
    path('exams/', views.exam, name='exam'),
    path('details_exam/', views.details_exam, name='details_exam'),
    path('edit_exam/', views.edit_exam, name='edit_exam'),
    path('gestion_exam/', views.gestion_exam, name='gestion_exam'),
    path('students/', views.student, name='student' ),
    path('students/editStudent/', views.editStudent, name='editStudent' ),
    path('students/getModels/', views.getModels, name='getModels' ),
    path('students/EditModels/', views.EditModels, name='EditModels' ),
    path('settings/', views.settings, name='settings' ),
    path('profile/', views.profile_admin, name='profile_admin' ),
 #   -------------------- paths etudiant -------------------- #
     path('etudiant/',views_etudiant.dashboard_s , name='dashboard_s'),

    path('etudiant/list_exam',views_etudiant.afficher_qcm , name='list_exam'),
    path('etudiant/passer_qcm',views_etudiant.passer_qcm , name='passer_qcm'),
    path('etudiant/resultat_qcm',views_etudiant.resultat_qcm , name='resultat_qcm'),
     path('etudiant/profile',views_etudiant.profile , name='profile'),
]