from django import forms
from django.contrib.auth.forms import UserCreationForm

from devpro.base.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]
