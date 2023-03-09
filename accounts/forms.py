from django import forms
from .models import Peep, Profile

class PeepForm(forms.ModelForm):
    body = forms.CharField(required=True, 
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "What am I up to today?",
                "class": "form-control",
            }
            ),
            label="",
        )
    
    class Meta:
        model = Peep
        exclude = ("user",)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image',]
        labels = {
            'profile_image': 'add image',

        }