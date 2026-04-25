
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass  # Make sure to import your form class

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form data
        print("in FormViewA")  # This message will print once
        return super(FormViewA, self).form_valid(form)  # Call parent implementation

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form data
        print("in FormViewB")  # This message will print first
        return super(FormViewB, self).form_valid(form)  # Call FormViewA's implementation
