
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass  # Assuming you have this form defined

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form data
        print("in FormViewA")  # Debug output
        return super().form_valid(form)  # Call parent's form_valid


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save again (if needed)
        print("in FormViewB")  # Debug output
        return super().form_valid(form)  # Call parent’s form_valid

# Usage:
# In your templates, when you submit the form handled by FormViewB,
# you'll see both outputs from FormViewA and FormViewB.
