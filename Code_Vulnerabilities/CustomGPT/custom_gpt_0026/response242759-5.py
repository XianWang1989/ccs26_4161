
# views.py
from django.shortcuts import redirect
from django.urls import reverse

class ArchitectDetailsView(View):
    def get(self, request):
        return render(request, 'architect_details.html')

    def post(self, request):
        # Handle data processing here
        return redirect('some_redirect_url')
