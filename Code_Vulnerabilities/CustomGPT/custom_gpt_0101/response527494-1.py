
# views.py
from django.shortcuts import render, redirect
from postman.models import Message
from postman.forms import MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
    else:
        form = MessageForm()
    return render(request, 'postman/send_message.html', {'form': form})

# urls.py
from django.urls import path
from .views import send_message

urlpatterns = [
    path('send/', send_message, name='send_message'),
]

# send_message.html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
