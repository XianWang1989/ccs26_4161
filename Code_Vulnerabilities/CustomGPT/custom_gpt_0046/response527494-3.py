
from django import forms
from postman.models import Message  # Adjust the model import

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
