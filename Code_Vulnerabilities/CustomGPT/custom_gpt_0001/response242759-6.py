
# forms.py

class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectDetails
        fields = ['business_name', 'license_number']  # Add fields according to your model

# views.py

from django.views import View
from django.shortcuts import render

class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectDetailsForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect after successful form submission
        return render(request, 'architect_details.html', {'form': form})
