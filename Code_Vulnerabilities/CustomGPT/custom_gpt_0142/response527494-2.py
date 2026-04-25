
from postman import views as postman_views
from django.shortcuts import render

def send_message_view(request):
    if request.method == 'POST':
        form = postman_views.MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to inbox or some confirmation page
            return redirect('postman:inbox')
    else:
        form = postman_views.MessageForm()

    return render(request, 'postman/send_message.html', {'form': form})
