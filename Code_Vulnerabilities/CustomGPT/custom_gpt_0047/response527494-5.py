
from postman.views import MessageCreationView

class CustomMessageCreationView(MessageCreationView):
    template_name = 'postman/send_message.html'
