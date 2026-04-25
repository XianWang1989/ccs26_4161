
from django.views.generic.edit import FormView
from django.urls import reverse

# Base form view
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form instance
        print("in FormViewA")  # Output from FormViewA
        return super(FormViewA, self).form_valid(form)  # Call superclass method

# Inherited form view
class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Additional save in FormViewB
        print("in FormViewB")  # Output from FormViewB
        return super(FormViewB, self).form_valid(form)  # Call FormViewA's method

# Usage in a template would specify FormViewB
