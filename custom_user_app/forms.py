from django import forms
from custom_user_app.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['displayname', 'homepage', 'age']
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)