
from django.views.generic.edit import FormView
from django.urls import reverse
from django import forms

# Define a simple form
class MyFormClass(forms.Form):
    name = forms.CharField(max_length=100)

# FormViewA definition
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Save the form data
        print("Saving form data in FormViewA")
        return super(FormViewA, self).form_valid(form)

# FormViewB inherits from FormViewA
class FormViewB(FormViewA):
    def form_valid(self, form):
        # Save the form data in the derived class
        print("Saving form data in FormViewB")
        return super(FormViewB, self).form_valid(form)

# In your HTML template (mytemplate.html), you'd have a form that submits to the view
