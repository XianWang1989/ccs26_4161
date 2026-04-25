
from django import forms
from postman.models import Message  # Adjust the import based on your setup

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']  # Adjust fields as necessary
