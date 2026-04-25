
# forms.py
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = Architect  # Define this model as per your requirements
        fields = ['business_name', 'license_number']  # Add fields as needed

# views.py
from django.shortcuts import render, redirect

def architect_details_view(request):
    if request.method == 'POST':
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after saving
    else:
        form = ArchitectDetailsForm()
    return render(request, 'architect_details.html', {'form': form})
