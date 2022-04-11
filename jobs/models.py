# Create your models here.
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.


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
        ('Remote-work', 'Remote-work'),
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

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='media/companies/')
    city = models.CharField(max_length=255)

    job_type = models.CharField(max_length=255, choices=job_choices)
    level_type = models.CharField(max_length=255, choices=level_choices)
    developer_type = models.CharField(
        max_length=255, choices=developer_choices)
    no_of_vacancies = models.PositiveIntegerField()
    deadline = models.DateTimeField()
    skills = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=20)
    description = RichTextField()

    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
