from django.urls import path
from core import views
from django.shortcuts import redirect

#from auth.views import UserProfile, Signup, PasswordChange, PasswordChangeDone, EditProfile

from django.contrib.auth import views as authViews 


    #! rename those paths obligatorily
    #! rename those paths obligatorily
    #! rename those paths obligatorily

urlpatterns = [

    path('', views.dashboard , name='dashboard'),
   	path('login/', authViews.LoginView.as_view(template_name='admine/pages/login.html'), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'login'}, name='logout'),
   	#path('changepassword/', PasswordChange, name='change_password'),
   	#path('changepassword/done', PasswordChangeDone, name='change_password_done'),

    path('students/', views.student, name='student' ),
    #path('students/addStudent/', views.addStudent, name='addStudent' ),
    #   path('students/deleteStudent/', views.deleteStudent, name='deleteStudent' ),  
    path('students/editStudent/', views.editStudent, name='editStudent' ),
    path('students/getModels/', views.getModels, name='getModels' ),
    path('students/EditModels/', views.EditModels, name='EditModels' ),


    path('exams/', views.exam, name='exam'),
    path('details_exam/', views.details_exam, name='details_exam'),
    path('edit_exam/', views.edit_exam, name='edit_exam'),
    path('gestion_exam/', views.gestion_exam, name='gestion_exam'),
    
    #? sestion for exams

    #path('exams/addExam/', views.addExam, name='addExam' ),
    #path('exams/deleteExam/', views.deleteExam, name='deleteExam' ),
    #path('exams/editExam/', views.editExam, name='editExam' ),

    path('settings/', views.settings, name='settings' ),
    #path('settings/editSettings/', views.editSettings, name='editSettings' ),

    #path('logout/', views.logoutUser, name='logout' ),
    #path('register/', views.registerPage, name='register' ),

 #   path('', lambda request: redirect('/', permanent=True)),
  
]