from django.db import models
from pip._vendor.rich.markup import Tag

from accounts.models import CustomUser
from vacancy.models import Vacancy


# Create your models here.

class Profile(models.Model):
    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    experience = models.FloatField(default=0)
    location = models.CharField(max_length=250)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    comf_salary = models.DecimalField(max_digits=10, decimal_places=2)
    birth_date = models.DateField()
    tags = models.TextField(blank=True, null=True)

class Click(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
