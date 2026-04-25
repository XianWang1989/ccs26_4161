
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Custom behavior before calling the superclass method
        print("Saving from FormViewA")
        return super().form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Custom behavior before calling the superclass method
        print("Saving from FormViewB")
        return super().form_valid(form)

# In your template, when the form is submitted, FormViewB will execute 
# and you'll see:
# Saving from FormViewB
# Saving from FormViewA
