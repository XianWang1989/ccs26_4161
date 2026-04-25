
from django.views.generic.edit import FormView

class ArchitectDetailsView(FormView):
    template_name = 'architect_details.html'
    form_class = ArchitectDetailsForm

    def form_valid(self, form):
        form.save()
        return redirect('home')  # Redirect after saving
