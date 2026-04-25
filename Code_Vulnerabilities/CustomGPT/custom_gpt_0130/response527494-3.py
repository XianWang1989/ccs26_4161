
from django.shortcuts import render
from postman.forms import WriteForm

def write_message(request):
    form = WriteForm()
    return render(request, 'write.html', {'form': form})
