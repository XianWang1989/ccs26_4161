
from django.views.generic import FormView

class BusinessDetailsView(FormView):
    template_name = 'business_details.html'
    form_class = BusinessDetailsForm

    def form_valid(self, form):
        form.save()
        return redirect('success-url')  # Redirect after saving the business details
