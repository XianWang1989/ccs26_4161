
from django import forms
from postman.models import Message  # Replace with your actual model

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']  # Adjust fields as necessary
