
# views.py
from django.shortcuts import render, redirect
from postman.views import SendMessageView

class CustomSendMessageView(SendMessageView):
    template_name = 'postman/send_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context if necessary
        return context
