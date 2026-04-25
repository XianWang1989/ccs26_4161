
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass:
    # Assume this is a valid Django form
    pass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Process the form data
        print("in FormViewA")
        return super().form_valid(form)  # Call parent method

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Additional processing
        print("in FormViewB")
        return super().form_valid(form)  # Call FormViewA's method

# When using FormViewB
view = FormViewB()
view.form_valid(form_instance)  # This will output both messages
