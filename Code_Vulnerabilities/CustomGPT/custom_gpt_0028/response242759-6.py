
# views.py
from django.views.generic.edit import CreateView

class ArchitectDetailsView(CreateView):
    model = ArchitectDetails
    form_class = ArchitectDetailsForm
    template_name = 'architect_details.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
