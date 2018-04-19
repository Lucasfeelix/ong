from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'last_name', 'username', 'email']


class UserAdminForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'last_name', 'is_active', 'is_staff']
