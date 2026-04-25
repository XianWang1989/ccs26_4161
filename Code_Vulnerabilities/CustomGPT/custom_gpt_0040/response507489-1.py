
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass  # Make sure to import your custom form

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # First form processing logic
        form.save()
        print("in FormViewA")
        return super().form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Additional processing for FormViewB
        form.save()
        print("in FormViewB")
        return super().form_valid(form)
