from django.forms import ModelForm
from .models import Bid
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BiddingForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']



class UserSignUpForm(UserCreationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "password")
    


