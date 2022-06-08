from django.urls import path
from candidate import views

urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="candi-home"),
    path("create/profile",views.CandidateProfileView.as_view(),name="can-profile")
]