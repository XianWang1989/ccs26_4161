
from postman.views import WriteMessageView

class CustomWriteMessageView(WriteMessageView):
    template_name = 'your_template_name.html'  # Adjust to your template
