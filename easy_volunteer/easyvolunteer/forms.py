from django import forms
from .models import CUser, Organ, Service, Area, Job, Product, Brand


class LoginForm(forms.ModelForm):
    class Meta:
        model = CUser
        fields - []

class UserF