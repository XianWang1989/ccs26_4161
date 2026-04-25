
from django.shortcuts import render
from postman import views as postman_views

def send_message_view(request, user_id):
    # You can get user details or other data if necessary
    recipient = get_user_model().objects.get(id=user_id)

    return render(request, 'send_message.html', {
        'recipient': recipient,
    })
