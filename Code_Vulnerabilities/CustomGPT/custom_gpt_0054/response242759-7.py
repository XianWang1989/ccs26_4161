
# forms.py (add this new form)
class ArchitectBusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = BusinessDetailsModel  # Define this model accordingly
        fields = ['business_name', 'business_address', ...]  # Your fields here

# views.py (add this new view)
@login_required
def architect_business_details(request):
    if request.method == 'POST':
        form = ArchitectBusinessDetailsForm(request.POST)
        if form.is_valid():
            business_details = form.save(commit=False)
            business_details.user = request.user
            business_details.save()
            return redirect('some_success_url')  # Redirect after saving
    else:
        form = ArchitectBusinessDetailsForm()

    return render(request, 'registration/business_details.html', {'form': form})
