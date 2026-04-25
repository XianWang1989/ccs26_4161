
# in your_app/views.py

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile_setup(request):
    user = request.user
    if user.user_type == 'arch' and not user.arch_details_completed:
        return redirect('architect_details')
    # other logic for redirecting or rendering page

def architect_details(request):
    if request.method == 'POST':
        # process architect details form
        pass
    return render(request, 'architect_details.html')  # Template for architect details
