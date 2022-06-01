from django import forms
from employer.models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class JobForm(forms.Form):
#     job_title=forms.CharField()
#     company=forms.CharField()
#     location=forms.CharField()
#     salary=forms.IntegerField()
#     experience=forms.IntegerField()
class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields="__all__"


class SighnupForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())