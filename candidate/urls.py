from django.urls import path
from candidate import views

urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name='candi-home'),
    path("create/profile",views.CandidateProfileView.as_view(),name="can-profile"),
    path("profile/detail",views.CandidateProfileDetailView.as_view(),name='can-pdetail'),
    path("update/profile",views.CandidateProfieEditView.as_view(),name='can-update'),
    path("list/jobs",views.CandidateJobListView.as_view(),name='list-job'),
    path("job/detail<int:id>",views.CandidateJobDetailView.as_view(),name='can-detailjob'),
    path("job/apply-now/<int:id>",views.apply_now,name='apply-now')
]