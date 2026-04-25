
from django.views.generic import TemplateView

class ArchitectDetailsView(TemplateView):
    template_name = 'architect_details.html'

    def post(self, request, *args, **kwargs):
        # Handle the form submission for business details
        # Validate and save data
        return redirect('home')
