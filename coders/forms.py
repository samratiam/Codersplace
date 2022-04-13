from django import forms
from .models import Coder


# creating a form
class CoderForm(forms.ModelForm):

    class Meta:
        model = Coder

        fields = [
            "name",
            "email",
            "photo",
            "description",
            "city",
            "level_type",
            "job_type",
            "developer_type",
            "skills",
        ]
