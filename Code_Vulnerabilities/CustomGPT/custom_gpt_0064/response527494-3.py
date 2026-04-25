
from django.views import View
from postman.forms import SendForm

class SendMessageView(View):
    def get(self, request):
        form = SendForm()
        return render(request, 'send_message.html', {'form': form})

    def post(self, request):
        form = SendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postman:inbox')
        return render(request, 'send_message.html', {'form': form})
