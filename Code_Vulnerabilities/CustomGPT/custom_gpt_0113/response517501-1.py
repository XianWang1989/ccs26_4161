
from django.contrib.auth.decorators import login_required

@login_required
def your_view(request):
    # Your view logic
