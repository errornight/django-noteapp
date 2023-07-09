from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Ticket


class UserSignup(UserCreationForm):
    profile = forms.ImageField(label='Profile Image:', required=False)

    class Meta:
        model = User
        fields = ['name', 'username', 'password1', 'password2', ]

class UserLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class EditProfile(forms.ModelForm):
    profile = forms.ImageField(label='Profile Image:', required=False)

    class Meta:
        model = User
        fields = ['name',]

class SendTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['answered']