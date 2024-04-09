from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class Signupform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = models.Account
        fields = ('email', 'username', 'password1', 'password2', 'contact', 'category')


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class UpdateResultForm(forms.ModelForm):
    english = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    bengali = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mathematics = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    science = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    programming = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    environment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = models.ResultDb
        fields = ( 'english', 'bengali', 'mathematics', 'science', 'programming', 'environment')
