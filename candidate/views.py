from django.shortcuts import render,redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView
from candidate.forms import CandidateProfileForm,CandidateProfileEditForm
from candidate.models import CandidateProfile
from employer.models import User
from employer.models import Jobs,Applications
from django.contrib import messages

class CandidateHomeView(TemplateView):
    template_name = "candidates/candi-home.html"


class CandidateProfileView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "candidates/can-profile.html"
    success_url = reverse_lazy('candi-home')
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"Your profile has been added")
        return super().form_valid(form)

class CandidateProfileDetailView(TemplateView):
    template_name = "candidates/can-profiledetails.html"


class CandidateProfieEditView(FormView):
    model=CandidateProfile
    template_name = "candidates/can-proedit.html"
    form_class = CandidateProfileEditForm

    def get(self, request, *args, **kwargs):
        profiles=CandidateProfile.objects.get(user=request.user)
        form=CandidateProfileEditForm(instance=profiles,initial={
            "first_name":request.user.first_name,
            "last_name":request.user.last_name,
            "phone":request.user.phone,
            "email":request.user.email
        })
        return render(request,self.template_name,{"form":form})

    def post(self, request, *args, **kwargs):
        profiles=CandidateProfile.objects.get(User=request.user)
        form=self.form_class(instance=profiles,data=request.POST,files=request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data.pop("first_name")
            last_name=form.cleaned_data.pop("last_name")
            phone=form.cleaned_data.pop("phone")
            email=form.cleaned_data.pop("email")
            form.save()
            user=User.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            user.phone=phone
            user.email=email
            user.save()
            return redirect('candi-home')
        else:
            return render(request,self.template_name,{"form":form})

class CandidateJobListView(ListView):
    model=Jobs
    context_object_name = "jobs"
    template_name = "candidates/joblist.html"

    def get_queryset(self):
        return self.model.objects.filter(active_status=True).order_by("created_date")

class CandidateJobDetailView(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "candidates/jobdetail.html"
    pk_url_kwarg = "id"


def apply_now(request,*args,**kwargs):
    user=request.user
    job_id=kwargs.get("id")
    jobs=Jobs.objects.get(id=job_id)
    Applications.objects.create(applicant=user,
                                job=jobs,
                                )
    messages.success(request,"your application submitted successfully")
    return redirect("candi-home")


