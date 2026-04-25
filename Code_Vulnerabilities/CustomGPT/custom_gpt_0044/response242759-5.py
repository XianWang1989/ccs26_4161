
from django.views import View
from django.shortcuts import render

class ArchitectBusinessDetailsView(View):
    def get(self, request):
        # Render business details form
        return render(request, 'architect_business_details.html')

    def post(self, request):
        # Handle form submission
        # Save business details here
        return redirect('home')
