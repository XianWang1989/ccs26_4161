
from django.views.generic.edit import FormView

class ArchitectDetailsView(FormView):
    template_name = 'architect_details.html'
    form_class = ArchitectDetailsForm  # Assume you create this form

    def form_valid(self, form):
        # Save the business details
        return super().form_valid(form)

    def get_success_url(self):
        return '/home/'  # Redirect to home or another page
