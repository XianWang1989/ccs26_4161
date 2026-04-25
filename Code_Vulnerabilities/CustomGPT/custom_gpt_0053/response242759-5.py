
# views.py
from django.shortcuts import redirect
from django.views import View

class ArchitectRegistrationView(View):
    def get(self, request):
        # Render the business details form
        return render(request, 'architect_registration.html')

    def post(self, request):
        # Handle business details form submission
        # Save the data
        return redirect('success_page')  # Redirect to a success page or dashboard
