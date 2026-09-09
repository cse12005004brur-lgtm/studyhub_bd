from django import forms
from django.contrib.auth.models import User
from .models import Note


class NoteForm(forms.ModelForm):

  class Meta:
    model = Note
    fields = ['title', 'student_class', 'subject', 'description', 'pdf_file']
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'student_class': forms.Select(attrs={'class': 'form-control'}),
        'subject': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        'pdf_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }


class UserRegistrationForm(forms.ModelForm):
  password = forms.CharField(
      widget=forms.PasswordInput(attrs={'class': 'form-control'}),
      label='Password',
  )
  confirm_password = forms.CharField(
      widget=forms.PasswordInput(attrs={'class': 'form-control'}),
      label='Confirm Password',
  )

  class Meta:
    model = User
    fields = ['first_name', 'email', 'password']
    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
    }

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    if password and confirm_password and password != confirm_password:
      raise forms.ValidationError('পাসওয়ার্ড দুটি মিলছে না!')
    return cleaned_data