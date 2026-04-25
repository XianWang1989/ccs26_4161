
class ArchitectDetailsForm(forms.Form):
    business_name = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=50)

def architect_details(request):
    if request.method == 'POST':
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            # Save additional details
            # Implement the logic to save data
            return redirect('home')
    else:
        form = ArchitectDetailsForm()
    return render(request, 'architect_details.html', {'form': form})
