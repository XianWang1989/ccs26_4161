
# views.py
from django.views import View
from django.shortcuts import render

class ArchitectDetailsView(View):
    def get(self, request):
        return render(request, 'architect_details.html')

    def post(self, request):
        # Handle form submission
        # Save business details
        return redirect('home')  # Redirect to a home page after submission
