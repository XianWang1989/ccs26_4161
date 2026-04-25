
from django.views import View
from django.shortcuts import render, redirect

class ArchitectDetailsView(View):
    def get(self, request):
        return render(request, 'architect_details.html')

    def post(self, request):
        # Handle form submission for business details
        # Save the data to the user's profile
        return redirect('account_login')  # or any other page
