
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass(forms.Form):
    # Define your form fields here
    pass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # Updated to Python 3 syntax
        return super().form_valid(form)  # Using modern syntax

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # Updated to Python 3 syntax
        return super().form_valid(form)  # Calls parent method
