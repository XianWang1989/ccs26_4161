
from django.shortcuts import render, redirect
from django.views import View
from .forms import ArchitectBusinessDetailsForm  # You will create this form

class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectBusinessDetailsForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectBusinessDetailsForm(request.POST)
        if form.is_valid():
            # Handle saving the form data here
            return redirect('home')  # Change to your desired redirect
        return render(request, 'architect_details.html', {'form': form})
