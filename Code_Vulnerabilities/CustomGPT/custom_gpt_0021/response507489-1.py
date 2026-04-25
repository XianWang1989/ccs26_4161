
from django.urls import reverse
from django.views.generic.edit import FormView
from .forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Save the form instance
        form.save()
        print("in FormViewA")
        return super().form_valid(form)  # Call the parent class's form_valid method

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Save the form instance specifically for FormViewB
        form.save()
        print("in FormViewB")
        return super().form_valid(form)  # Call FormViewA's form_valid method

# Usage of FormViewB in a URLconf would trigger both prints upon form submission.
