from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Coder(models.Model):
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
    photo = models.ImageField(upload_to='media/coders/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    level_type = models.CharField(max_length=255, choices=level_choices)
    job_type = models.CharField(max_length=255, choices=job_choices)
    developer_type = models.CharField(
        max_length=255, choices=developer_choices)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name
