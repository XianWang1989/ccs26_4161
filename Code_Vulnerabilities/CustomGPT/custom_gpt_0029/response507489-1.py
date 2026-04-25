
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass  # Assume MyFormClass is defined in your forms.py

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Save the form data
        form.save()
        print("in FormViewA")
        # Call the parent class's form_valid method
        return super().form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Save the form data
        form.save()
        print("in FormViewB")
        # Call the parent class's form_valid method
        return super().form_valid(form)
