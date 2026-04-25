
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('post/send/', views.send_message_view, name='post_message'),
]

# views.py
from django.shortcuts import render
from postman import views as postman_views
from django.shortcuts import redirect

def send_message_view(request):
    if request.method == 'POST':
        form = postman_views.MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
    else:
        form = postman_views.MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})

# templates/postman/send_message.html
<h2>Send a Message</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send Message</button>
</form>

# Update your navigation links
<li><a href="{% url 'post_message' %}">Send Message</a></li>
