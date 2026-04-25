
from django.views.generic import FormView
from .forms import ArchitectDetailsForm  # Create your form for business details

class ArchitectDetailsView(FormView):
    template_name = 'architect_details.html'
    form_class = ArchitectDetailsForm

    def form_valid(self, form):
        # Save the business details
        return super().form_valid(form)

    def get_success_url(self):
        return '/success/'  # Redirect to a success page
