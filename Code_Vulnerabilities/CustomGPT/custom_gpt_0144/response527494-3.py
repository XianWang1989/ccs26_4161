# forms.py
from django import forms
from postman.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body', 'recipient']  # Adjust as necessary for your Message model
