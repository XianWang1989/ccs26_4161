
# yourapp/views.py

from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from .forms import ArchitectDetailsForm

class UserSignupView(View):
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the registered user
        if user.user_type == 'Architect':
            return redirect(reverse('architect_details'))

    def get(self, request, *args, **kwargs):
        # Handle GET request if needed
        return super().get(request, *args, **kwargs)

class ArchitectDetailsView(View):
    def get(self, request, *args, **kwargs):
        form = ArchitectDetailsForm()  # Initialize your architect details form
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            # Save architect details
            return redirect('home')  # Redirect to home or another page
