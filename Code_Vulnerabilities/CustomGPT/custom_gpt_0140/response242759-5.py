
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = Architect
        fields = ['business_name', 'license_number', 'website']

def architect_details_view(request):
    if request.method == 'POST':
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = ArchitectDetailsForm()
    return render(request, 'architect_details.html', {'form': form})
