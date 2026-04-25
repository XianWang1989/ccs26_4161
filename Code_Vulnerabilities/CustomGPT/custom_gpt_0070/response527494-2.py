
from postman.views import SendMessageView

class CustomSendMessageView(SendMessageView):
    template_name = 'your_template.html'  # Customize the template if needed
