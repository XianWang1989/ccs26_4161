
from postman.models import Message

def write_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # handle success
    else:
        form = MessageForm()

    return render(request, 'postman/write.html', {'form': form})
