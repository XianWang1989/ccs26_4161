
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = Architect  # Create an Architect model to store details
        fields = ['business_name', 'license_number', 'portfolio_link']

class ArchitectDetailsView(FormView):
    form_class = ArchitectDetailsForm
    template_name = 'architect_details.html'

    def form_valid(self, form):
        form.save()
        return redirect('home')  # Redirect after successful save
