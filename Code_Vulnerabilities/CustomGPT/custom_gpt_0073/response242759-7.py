
# myapp/views.py
from django.views import View
from django.shortcuts import render

class ArchitectDetailsView(View):
    def get(self, request):
        # Render your form here
        return render(request, 'architect_details.html')

    def post(self, request):
        # Handle form submission here
        pass
