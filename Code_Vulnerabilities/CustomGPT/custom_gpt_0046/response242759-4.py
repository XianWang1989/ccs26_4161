
# views.py
class ArchitectDetailsView(View):
    def get(self, request):
        # Render form for architect details
        return render(request, 'architect_details.html')

    def post(self, request):
        # Handle form submission for architect details
        # Save the details as needed
        return redirect('home')  # Redirect to the home page or any desired location
