from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Ticket


class UserSignup(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password1', 'password2', 'profile']

class UserLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'profile']

class SendTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['answered']