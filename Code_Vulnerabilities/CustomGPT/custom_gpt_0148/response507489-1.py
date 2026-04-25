
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Saves the form
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)  # Calls the superclass method


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Saves the form again
        print("in FormViewB")
        return super(FormViewB, self).form_valid(form)  # Calls FormViewA's form_valid


# Usage in views.py
# To use FormViewB, you would set up a URL and template similarly.
