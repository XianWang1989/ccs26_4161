
from postman.views import SendView
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request):
    return SendView.as_view()(request)
