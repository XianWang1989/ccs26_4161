
from django.views.generic.edit import FormView
from .forms import BusinessDetailsForm  # Define this form

class BusinessDetailsView(FormView):
    template_name = 'business_details.html'
    form_class = BusinessDetailsForm
    success_url = '/success/'  # Set where to redirect after submission

    def form_valid(self, form):
        # Save the business details
        form.save()
        return super().form_valid(form)
