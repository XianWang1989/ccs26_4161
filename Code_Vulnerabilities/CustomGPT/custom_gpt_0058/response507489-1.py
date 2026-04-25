
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
        print("in FormViewA")  # Output when FormViewA's form_valid is called
        return super(FormViewA, self).form_valid(form)  # Call the parent class's form_valid

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form data again (another save)
        print("in FormViewB")  # Output when FormViewB's form_valid is called
        return super(FormViewB, self).form_valid(form)  # This calls FormViewA's form_valid
