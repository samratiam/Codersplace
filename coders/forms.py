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
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            # 'photo':forms.FileInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'level_type':forms.Select(attrs={'class':'form-control'}),
            'job_type':forms.Select(attrs={'class':'form-control'}),
            'developer_type':forms.Select(attrs={'class':'form-control'}),
            'skills':forms.TextInput(attrs={'class':'form-control'}),
        }
