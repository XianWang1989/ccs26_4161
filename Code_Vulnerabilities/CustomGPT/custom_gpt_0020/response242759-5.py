
from django.views.generic.edit import FormView
from yourapp.forms import ArchitectDetailsForm

class ArchitectDetailsView(FormView):
    template_name = 'architect_details.html'
    form_class = ArchitectDetailsForm
    success_url = 'your_success_redirect_url'  # Define your success URL

    def form_valid(self, form):
        # Handle form submission, save business details
        form.save()
        return super().form_valid(form)
