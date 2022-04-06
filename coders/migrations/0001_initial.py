# Generated by Django 4.0.2 on 2022-02-07 04:48

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/coders/')),
                ('video_url', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('city', models.CharField(max_length=255)),
                ('level_type', models.CharField(choices=[('fresher', 'fresher'), ('junior', 'junior'), ('mid-level', 'mid-level'), ('senior', 'senior')], max_length=255)),
                ('job_type', models.CharField(choices=[('part-time', 'part-time'), ('full-time', 'full-time'), ('remote-work', 'remote-work'), ('intership', 'internship')], max_length=255)),
                ('developer_type', models.CharField(choices=[('.NET', '.NET'), ('React', 'React'), ('Nodejs', 'Nodejs'), ('PHP', 'PHP'), ('Laravel', 'Laravel'), ('Angular', 'Angular'), ('Django', 'Django')], max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]