
from django.contrib.auth import logout

def my_logout_view(request):
    logout(request)
    return redirect('home')  # Update with your homepage URL
