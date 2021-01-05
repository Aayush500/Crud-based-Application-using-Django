from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'autofocus': 'autofocus', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'password': forms.PasswordInput(render_value= True ,attrs={'placeholder': 'Enter your password', 'class': 'form-control'})
        }