from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import TemplateView,CreateView
from candidate.forms import CandidateProfileForm
from candidate.models import CandidateProfile

class CandidateHomeView(TemplateView):
    template_name = "candidates/candi-home.html"


class CandidateProfileView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "candidates/can-profile.html"
    success_url = reverse_lazy("candi-home")
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
