
# Inside your Django view
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, this is a test response!")
