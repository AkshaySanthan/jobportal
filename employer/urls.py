from django.urls import path
from employer import views


urlpatterns = [
   path('home',views.EmployerHomeView.as_view(),name="emp-home"),
    path('job/add',views.AddJobView.as_view(),name="emp-addjob"),
    path('jobs/all',views.ListJobView.as_view(),name='all-jobs'),
    path('job/details/<int:id>',views.JobDetailView.as_view(),name='job-details'),
    path('jobs/change/<int:id>',views.JobEditView.as_view(),name='job-edit'),
    path('jobs/remove/<int:id>',views.JobDeleteView.as_view(),name='job-delete'),
    path('user/account/sighnup',views.SighnupView.as_view(),name='sighnup'),
    path('user/account/sighnin',views.SighnInView.as_view(),name='sighnin'),
    path('user/account/sighnout',views.sighnout_view,name='sighnout'),
    path('user/change/password',views.ChangePasswordView.as_view(),name='passchange'),
    path('user/reset/password',views.PasswordResetView.as_view(),name='password-reset'),
    path('profile/add',views.CompanyProfileView.as_view(),name='emp-addprofile'),
    path('profile/view',views.EmpViewProfileView.as_view(),name='emp-profileview'), #no need of id becoz of having related name
    path('profile/edit/<int:id>',views.EmpEditProfileView.as_view(),name='emp-editprofile'),
    path("applications/list/<int:id>",views.EmployeeListApplications.as_view(),name='emp-app-list'),
    path("applications/detail<int:id>",views.EmployeeApplicationDetailView.as_view(),name='emp-app-detail')

   ]

# get and list=safe operation
