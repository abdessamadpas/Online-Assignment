from django.urls import path
from core import views
from django.shortcuts import redirect


urlpatterns = [

    path('dashboard/', views.dashboard , name='dashboard'),
    path('login/', views.loginPage, name='login' ),
    path('students/', views.PageStudents, name='PageStudents' ),
    path('students/editStudent/', views.editStudent, name='editStudent' ),
    path('students/getModels/', views.getModels, name='getModels' ),
    path('students/EditModels/', views.EditModels, name='EditModels' ),
    path('settings/', views.settings, name='settings' ),

    path('', lambda request: redirect('dashboard/', permanent=True)),
  
]