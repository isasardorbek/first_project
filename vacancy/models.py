from django.db import models

from accounts.models import CustomUser


# Create your models here.

class Vacancy(models.Model):
    REMOTE_TYPE = (
        ('R', 'Remote'),
        ('O', 'Office'),
        ('H', 'Hybrid')
    )
    WORK_TYPE = (
        ('F', 'Full time'),
        ('P', 'Part time')
    )

    job_poster= models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    location = models.CharField(max_length=100)
    min_exp = models.FloatField(default=0)
    max_exp = models.FloatField(null=True, blank=True)
    title = models.CharField(max_length=100)
    type_remote = models.CharField(choices=REMOTE_TYPE,max_length=1, null=True, blank=True)
    type_work = models.CharField(choices=WORK_TYPE,max_length=1, null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    tags = models.TextField()