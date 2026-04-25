
from django.views import View
from django.shortcuts import render, redirect
from postman.forms import MessageForm

class SendMessageView(View):
    def get(self, request):
        form = MessageForm()
        return render(request, 'send_message.html', {'form': form})

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
        return render(request, 'send_message.html', {'form': form})
