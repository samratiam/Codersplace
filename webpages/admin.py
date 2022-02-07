import imp
from django.contrib import admin
from .models import Slider, Team, Contact
# Register your models here.

admin.site.register(Slider)
admin.site.register(Team)
admin.site.register(Contact)