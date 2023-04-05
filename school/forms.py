from django import forms
from .models import Student

## Here we'll use Model and It's attributes/fields to create a ModelForm
## Then this ModelForm will be used in our class in views.py
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myclass'}),
            'email': forms.EmailInput(attrs={'class': 'myemail'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'mypass'}),
        }