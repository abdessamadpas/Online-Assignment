from django.urls import path
from core import views , views_etudiant
from django.shortcuts import redirect
from core.views.crud_Student.add_listStudent import add_listStudent
from core.views.crud_Student.put_delete_Student import put_delete_Student
#from auth.views import UserProfile, Signup, PasswordChange, PasswordChangeDone, EditProfile
from core.views.auth.customLogin import RoleBasedLoginView

from django.views.generic import TemplateView

from django.contrib.auth import views as authViews 


    #! rename those paths obligatorily
    #! rename those paths obligatorily
    #! rename those paths obligatorily

urlpatterns = [


   	path('login/', RoleBasedLoginView.as_view(), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'login'}, name='logout'),
    path('admin_dasboard/', views.dashboard , name='dashboarde'),

    path('access_denied_student/', TemplateView.as_view(template_name="public/access_denied.html"), name='access_denied_student'),
    path('', views.dashboard , name='dashboard'),
   	#path('login/', authViews.LoginView.as_view(template_name='admine/pages/login.html'), name='login'),
   	#path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'login'}, name='logout'),

   	#path('changepassword/', PasswordChange, name='change_password'),
   	#path('changepassword/done', PasswordChangeDone, name='change_password_done'),

    path('students/', views.student, name='student' ),
    
    #? api for add student 
    path('students/add_list_Student/',add_listStudent.as_view(), name='addStudent' ),
    path('students/put_delete_Student/<int:pk>', put_delete_Student.as_view(), name='deleteStudent'),
    #path('students/addStudent/', views.addStudent, name='addStudent' ),
    #   path('students/deleteStudent/', views.deleteStudent, name='deleteStudent' ),  
    path('students/editStudent/', views.editStudent, name='editStudent' ),
    path('students/getModels/', views.getModels, name='getModels' ),
    path('students/EditModels/', views.EditModels, name='EditModels' ),

    #? modules section
   # path('<module_id>/', CourseDetail, name='course'),
    #path('<module_id>/', CourseDetail, name='course'),
	#path('<modele_id>/enroll', Enroll, name='enroll'),
	#path('<modele_id>/edit', EditCourse, name='edit-course'),
	#path('<modele_id>/delete', DeleteCourse, name='delete-course'),



    path('exams/', views.exam, name='exam'),
    path('details_exam/', views.details_exam, name='details_exam'),
    path('edit_exam/', views.edit_exam, name='edit_exam'),
    path('gestion_exam/', views.gestion_exam, name='gestion_exam'),
    
    #? exams sestion 

    #path('exams/addExam/', views.addExam, name='addExam' ),
    #path('exams/deleteExam/', views.deleteExam, name='deleteExam' ),
    #path('exams/editExam/', views.editExam, name='editExam' ),

    path('settings/', views.settings, name='settings' ),
    path('profile/', views.profile_admin, name='profile_admin' ),
 #   -------------------- paths etudiant -------------------- #



    #path('settings/editSettings/', views.editSettings, name='editSettings' ),

    #path('logout/', views.logoutUser, name='logout' ),
    #path('register/', views.registerPage, name='register' ),
    
    #!  etudent paths 
    #? take care of the paths and views functions  
    path('etudiant/',views_etudiant.dashboard_s , name='dashboard_s'),
    path('etudiant/list_exam',views_etudiant.afficher_qcm , name='list_exam'),
    path('etudiant/passer_qcm/<module_id>/<exam_id>',views_etudiant.passer_qcm , name='passer_qcm'),
    path('etudiant/resultat_qcm',views_etudiant.resultat_qcm , name='resultat_qcm'),
     path('etudiant/profile',views_etudiant.profile , name='profile'),
]