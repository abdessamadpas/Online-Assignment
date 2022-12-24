
from django.contrib import admin
from django.urls import path
from core import views
from django.shortcuts import redirect

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('students/', views.PageStudents, name='PageStudents' ),
    path('students/editStudent/', views.editStudent, name='editStudent' ),
    path('students/getModels/', views.getModels, name='getModels' ),
    path('students/EditModels/', views.EditModels, name='EditModels' ),
    path('settings/', views.settings, name='settings' ),
    #path('', lambda request: redirect('studentDashboard/students/', permanent=True))

]

