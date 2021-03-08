from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class UserImageUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']