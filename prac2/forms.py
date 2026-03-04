from django import forms
from .models import student

class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'age']

  
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 5:
            raise forms.ValidationError("Age must be greater than 5.")
        return age