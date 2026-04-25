
# views.py (continued)
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    # (previous code...)

    def form_valid(self, form):
        user = form.save(self.request)
        if form.cleaned_data['user_type'] == 'architect':
            return redirect('architect_details')  # URL for architect details page
        return super().form_valid(form)

# Create an architect details form and view
# forms.py
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectProfile  # Your model
        fields = ['business_name', 'license_number']  # Example fields

# views.py
class ArchitectDetailsView(CreateView):
    form_class = ArchitectDetailsForm
    template_name = 'architect_details.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Link to the logged-in user
        return super().form_valid(form)

# urls.py (continued)
urlpatterns += [
    path('accounts/architect-details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
