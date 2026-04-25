
# forms.py
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectProfile  # Your model for additional details
        fields = ['business_name', 'license_number']  # Add your fields here

# views.py
def architect_details(request):
    if request.method == 'POST':
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            architect_profile = form.save(commit=False)
            architect_profile.user = request.user  # Link to the user
            architect_profile.save()
            return redirect('home')
    else:
        form = ArchitectDetailsForm()
    return render(request, 'architect_details.html', {'form': form})
