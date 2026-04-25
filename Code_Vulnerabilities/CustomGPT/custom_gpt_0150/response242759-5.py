
# views.py
from django.views import View
from django.shortcuts import render

class ArchitectDetailsView(View):
    def get(self, request):
        # Render the architect details form
        return render(request, 'architect_details.html')

    def post(self, request):
        # Handle the form submission for business details
        # Process and save business details
        return redirect('success_url')  # Redirect after saving
