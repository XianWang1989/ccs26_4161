
# forms.py
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectProfile  # Replace with your model
        fields = ['business_name', 'license_number']  # Add your fields here

# views.py
class ArchitectDetailsView(View):
    def get(self, request):
        form = ArchitectDetailsForm()
        return render(request, 'architect_details.html', {'form': form})

    def post(self, request):
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after saving
        return render(request, 'architect_details.html', {'form': form})
