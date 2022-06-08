from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView
from employer.forms import JobForm,CompanyProfileForm
from employer.models import Jobs,CompanyProfile
from employer.forms import SighnupForm,LoginForm
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from employer.models import User

# Create your views here.

class EmployerHomeView(TemplateView):
    template_name="emp-home.html"


class AddJobView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-addjob.html"
    success_url = reverse_lazy('all-jobs')
    def form_valid(self, form):
        form.instance.company=self.request.user
        return super().form_valid(form)
    # def get(self,request):
    #     form=JobForm()
    #     return render(request,"emp-addjob.html",{"form":form})
    # def post(self,request):
    #     form=JobForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # jname=form.cleaned_data.get("job_title")
    #         # cname=form.cleaned_data.get("company")
    #         # location=form.cleaned_data.get("location")
    #         # salary=form.cleaned_data.get("salary")
    #         # exp=form.cleaned_data.get("experience")
    #         # Jobs.objects.create(
    #         #     job_title=jname,
    #         #     company_name=cname,
    #         #     location=location,
    #         #     salary=salary,
    #         #     experience=exp,
    #         # )
    #
    #         return render(request,"emp-home.html")
    #     else:
    #         return render(request,"emp-addjob.html",{"form":form})



class ListJobView(ListView):
    model=Jobs
    context_object_name = "jobs"
    template_name = "emp-listjob.html"
    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user)
        # return Jobs.objects.filter(company=self.request.user)


class JobDetailView(DetailView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-detailjob.html"
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,"emp-detailjob.html",{'job':qs})

class JobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-editjob.html"
    success_url = reverse_lazy("all-jobs")
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(instance=qs)
    #     return render(request,"emp-editjob.html",{"form":form})
    #
    # def post(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('all-jobs')
    #     else:
    #         return render(request,"emp-editjob",{"form":form})


class JobDeleteView(DeleteView):
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     qs.delete()
    #     return redirect('all-jobs')
    template_name = "jobdeleteconfi.html"
    success_url = reverse_lazy("all-jobs")
    pk_url_kwarg = "id"
    model = Jobs

class SighnupView(CreateView):
    model=User
    form_class = SighnupForm
    template_name = "usersighnup.html"
    success_url = reverse_lazy('sighnin')


class SighnInView(FormView):
    form_class = LoginForm
    template_name = "login.html"


    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                if request.user.role=="employer":
                    return redirect("all-jobs")
                elif request.user.role=="candidate":
                    return redirect("candi-home")

            else:
                return render(request,"login.html",{"form":form})

def sighnout_view(request,*args,**kwargs):
    logout(request)
    return redirect("sighnin")


class ChangePasswordView(TemplateView):
    template_name = "pwdchange.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect('password-reset')
        else:
            return render(request,self.template_name)


class PasswordResetView(TemplateView):
    template_name = "resetpass.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")
        if pwd1 != pwd2:
            return render(request,self.template_name,{"msg":'password mismatching'})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect('sighnin')

class CompanyProfileView(CreateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "emp-addprofile.html"
    success_url = reverse_lazy("emp-home")
    # def post(self, request, *args, **kwargs):
    #     form=CompanyProfileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         return redirect("emp-home")
    #     else:
    #         return render(request,self.template_name,{"form":form})
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class EmpViewProfileView(TemplateView):
    template_name = "emp-viewprofile.html"


class EmpEditProfileView(UpdateView):
    model=CompanyProfile
    form_class = CompanyProfileForm
    template_name = "emp-editprofile.html"
    success_url = reverse_lazy('emp-profileview')
    pk_url_kwarg = "id"
