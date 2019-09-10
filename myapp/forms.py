from django import forms
from myapp.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = UserProfile
        fields = "__all__"
