
from django.shortcuts import render, redirect
from postman import views as postman_views

def send_message(request):
    if request.method == 'POST':
        # Here you handle the sending logic: using Postman's send function.
        postman_views.send(request)
        return redirect('postman:inbox')  # Redirect after sending
    return render(request, 'your_template.html')
