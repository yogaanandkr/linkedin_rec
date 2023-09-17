from django import forms

from .models import Bio 



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Bio 
        fields = ['bio', 'profile_pic']