
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form data
        print("in FormViewA")
        return super().form_valid(form)  # Call the parent class's form_valid method

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form data again
        print("in FormViewB")
        return super().form_valid(form)  # Call FormViewA's form_valid method

# Usage
# If you use FormViewB, you will see:
# "in FormViewB"
# "in FormViewA"
