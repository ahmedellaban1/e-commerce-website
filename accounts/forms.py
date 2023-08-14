from .models import Profile, User
from django import forms


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'image', 'date_of_birth', 'country']
