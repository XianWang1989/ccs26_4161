
# views.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def additional_info(request):
    if request.method == 'POST':
        # Process additional business details here
        # e.g., save to a related model
        return redirect('home')  # Redirect to home or any specific page

    return render(request, 'additional_info.html')
