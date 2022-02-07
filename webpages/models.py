from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    linkedin_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/team/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'media/slider/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email



