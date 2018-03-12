from django import forms
from .models import Message
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User

class ComposeMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body', 'recipient')
