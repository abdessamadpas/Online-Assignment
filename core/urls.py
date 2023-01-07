from django.urls import path
from core import views
from django.shortcuts import redirect


urlpatterns = [

    path('', views.dashboard , name='dashboard'),
    path('login/', views.loginPage, name='login' ),
    path('exams/', views.exam, name='exam'),
    path('details_exam/', views.details_exam, name='details_exam'),
    path('gestion_exam/', views.gestion_exam, name='gestion_exam'),
    path('students/', views.student, name='student' ),
    path('students/editStudent/', views.editStudent, name='editStudent' ),
    path('students/getModels/', views.getModels, name='getModels' ),
    path('students/EditModels/', views.EditModels, name='EditModels' ),
    path('settings/', views.settings, name='settings' ),

 #   path('', lambda request: redirect('/', permanent=True)),
  
]