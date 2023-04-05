from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms
from .forms import StudentForm

# class StudentCreateView(CreateView):
#     model = Student # Create a form for Student model (automatically)
#     fields = ['name', 'email', 'password'] # Pass list of values to the form's attributes
#     template_name = 'school/student_form.html' # we must provide the template with "_form" suffix
#     # template_name = 'school/my_custom.html' # we can also provide custom template_name (without any suffix)
#     success_url = '/thankyou/' # Upon submitting the form, it will redirect to this "success_url" 

#     # add or modify css/bootstrap classes in form (We can also add classes in forms.py in ModelForm Class)
#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class':'myclass'})
#         return form

# CRUD using ModelForm Class
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    # success_url = '/thankyou/' # I have used 'get_absolute_url()' in models.py

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate/'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'school/student_delete.html'
    # success_url = '/create/' # Upon deleting, it will redirect to "Student Create" page
    success_url = '/delete/' # Upon deleting, it will redirect to "delete" page

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanksupdate.html'

class ThankyouTemplateView(TemplateView):
    template_name = 'school/thankyou.html'

class DeleteTemplateView(TemplateView):
    template_name = 'school/del.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student_detail.html'
