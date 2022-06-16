from django import forms
from employer.models import Jobs,CompanyProfile
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from employer.models import User

# class JobForm(forms.Form):
#     job_title=forms.CharField()
#     company=forms.CharField()
#     location=forms.CharField()
#     salary=forms.IntegerField()
#     experience=forms.IntegerField()
class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        # fields="__all__"
        exclude=("company","created_date","active_status")
        widgets={
            "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }





class SighnupForm(UserCreationForm):

    class Meta:
        # password1=forms.CharField(widget=forms.PasswordInput(attrs='class':'col-')
        model=User
        fields=["username","first_name","last_name","email","password1","password2","role","phone"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control rounded-pill"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control "}),
            "password2": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control rounded-pill"}),

        }



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    # widgets={
    #     "username":forms.TextInput(attrs={"class":"form-control"}),
    #     "password":forms.PasswordInput(attrs={"class":"form-control bg-danger"})
    # }



class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model=CompanyProfile
        exclude=("user",)
        widgets={
            "company_name":forms.TextInput(attrs={"class":"form-control rounded-pill"})

        }