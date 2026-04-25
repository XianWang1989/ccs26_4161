
from django.views.generic.edit import CreateView

class ArchitectDetailsView(CreateView):
    form_class = ArchitectDetailsForm
    template_name = 'architect_details.html'

    def form_valid(self, form):
        form.save(commit=False).user = self.request.user
        form.save()
        return redirect('success_url')
