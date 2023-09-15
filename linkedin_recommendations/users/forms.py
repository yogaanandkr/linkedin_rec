from django import forms

from .models import Bio 



class ProfileForm(forms.ModelForm):
    model = Bio 
    fields = '__all__'