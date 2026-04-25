
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

def signup_view(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'architect':
            return redirect('architect_details')
    return super().signup_view(request)

# Create a view for the additional details
class ArchitectDetailsView(TemplateView):
    template_name = 'architect_details.html'

    def post(self, request):
        # Handle form submission for architect's business details
        # Save the details as needed
        return redirect('home')
