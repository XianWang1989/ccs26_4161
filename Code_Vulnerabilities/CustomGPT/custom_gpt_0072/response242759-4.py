
# forms.py
class ArchitectDetailsForm(forms.Form):
    business_name = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=50)

# views.py
def architect_details_view(request):
    if request.method == 'POST':
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            # Save the details, then redirect
            return redirect('success_page')  # Redirect after save
    else:
        form = ArchitectDetailsForm()
    return render(request, 'architect_details.html', {'form': form})
