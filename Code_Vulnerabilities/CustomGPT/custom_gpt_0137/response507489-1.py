
from django.views.generic.edit import FormView
from django.urls import reverse

# Your form class, let's imagine it's defined somewhere
class MyFormClass(forms.Form):
    # Define your form fields here
    pass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form
        print("in FormViewA")  # Print from A
        return super(FormViewA, self).form_valid(form)  # Call the parent class method

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form again (if needed, might not be necessary)
        print("in FormViewB")  # Print from B
        return super(FormViewB, self).form_valid(form)  # Call FormViewA's method
