
from postman.views import send as postman_send

def send_message_view(request):
    # Custom logic here if needed
    return postman_send(request)
