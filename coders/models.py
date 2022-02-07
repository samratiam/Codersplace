from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Coder(models.Model):
    level_choices = (
        ('fresher','fresher'),
        ('junior','junior'),
        ('mid-level','mid-level'),
        ('senior','senior'),
    )

    job_choices = (
        ('part-time','part-time'),
        ('full-time','full-time'),
        ('remote-work','remote-work'),
        ('intership','internship'),
    )

    developer_choices = (
            ('.NET','.NET'),
            ('React','React'),
            ('Nodejs','Nodejs'),
            ('PHP','PHP'),
            ('Laravel','Laravel'),
            ('Angular','Angular'),
            ('Django','Django'),
        )

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'media/coders/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    level_type = models.CharField(max_length=255, choices=level_choices)
    job_type = models.CharField(max_length=255,choices=job_choices)
    developer_type = models.CharField(max_length=255,choices=developer_choices)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)