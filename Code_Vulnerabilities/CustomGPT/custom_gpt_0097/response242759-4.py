
# views.py
class ArchitectRegistrationView(View):
    def get(self, request):
        # Render your form for business details
        return render(request, 'architect_registration.html')

    def post(self, request):
        # Handle form submission
        pass
