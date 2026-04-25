
from django import forms
from postman.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'message', 'recipients']  # Add any additional fields necessary
