
# views.py
from postman import views as postman_views
from django.urls import reverse

def send_message_view(request):
    if request.method == 'POST':
        # Handle the form submission
        return postman_views.send_message(request)

    # Render the compose message form
    return postman_views.compose_view(request)
