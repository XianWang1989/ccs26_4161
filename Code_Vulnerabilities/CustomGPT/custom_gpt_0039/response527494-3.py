
from django.views.generic import TemplateView
from postman.forms import MessageForm

class SendMessageView(TemplateView):
    template_name = 'send_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context
