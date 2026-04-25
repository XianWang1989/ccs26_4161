
# forms.py (add this in the same file)
class ArchitectDetailsForm(forms.Form):
    business_name = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=50)
    # Add other fields as necessary

# views.py (add the new view)
from django.shortcuts import render

class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectDetailsForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            # Process the form data here
            # Save additional details if needed
            return redirect(reverse('home'))  # Redirect after processing
        return render(request, 'architect_details.html', {'form': form})
