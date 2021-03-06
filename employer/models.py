from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    options=(
        ("employer","employer"),
        ("candidate","candidate")
    )
    role=models.CharField(max_length=120,choices=options,default="candidate")
    phone=models.CharField(max_length=12,null=True)






class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company=models.ForeignKey(User,on_delete=models.CASCADE,related_name="company")
    location=models.CharField(max_length=120)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)
    created_date=models.DateField(auto_now_add=True)
    last_date=models.DateField(null=True)
    active_status=models.BooleanField(default=True)
    job_description=models.TextField(null=True)



    def __str__(self):
        return self.job_title




class CompanyProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="employer")
    company_name=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    services=models.CharField(max_length=150)
    logo=models.ImageField(upload_to="companyprofile",null=True)


class Applications(models.Model):
    applicant=models.ForeignKey(User,on_delete=models.CASCADE,related_name="applicant")
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    options=(
        ("applied","applied"),
        ("accepted","accepted"),
        ("rejected0","rejected"),
        ("pending","pending"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="applied")
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together= ("applicant","job")





