# Create your models here.
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.forms import DateInput
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/companies/')
    
    def __str__(self):
        return self.name
        
class Job(models.Model):

    level_choices = (
        ('Fresher', 'Fresher'),
        ('Junior', 'Junior'),
        ('Mid-level', 'Mid-level'),
        ('Senior', 'Senior'),
    )

    job_choices = (
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time'),
        ('Internship', 'Internship'),
    )

    developer_choices = (
        ('.NET', '.NET'),
        ('React', 'React'),
        ('Nodejs', 'Nodejs'),
        ('PHP', 'PHP'),
        ('Laravel', 'Laravel'),
        ('Angular', 'Angular'),
        ('Django', 'Django'),
    )
    
    company = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True)
    
    title = models.CharField(max_length=255, null=True)
    

    job_type = models.CharField(max_length=255, choices=job_choices)
    level_type = models.CharField(max_length=255, choices=level_choices)
    developer_type = models.CharField(
        max_length=255, choices=developer_choices)
    no_of_vacancies = models.PositiveIntegerField()
    deadline = models.DateField()
    skills = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=20)
    description = RichTextField()
    cosinevalue = models.FloatField(null=True,blank=True)
    is_featured = models.BooleanField(default=False)

    created_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.title
