
# forms.py
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectProfile  # Assuming you have a model for Architect
        fields = ['business_name', 'license_number']  # Add respective fields

# views.py
from django.views import View

class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectDetailsForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            architect = form.save(commit=False)
            architect.user = request.user
            architect.save()
            return redirect('home')  # Redirect after saving
        return render(request, 'architect_details.html', {'form': form})
