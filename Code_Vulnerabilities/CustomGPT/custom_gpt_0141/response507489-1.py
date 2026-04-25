
# views.py
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass  # Assuming you've defined MyFormClass in forms.py

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')  # Redirect to 'my_url' after form submission

    def form_valid(self, form):
        form.save()  # Save the form instance to the database
        print("in FormViewA")  # Output to console
        return super(FormViewA, self).form_valid(form)  # Call the parent's form_valid

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form instance in the child class
        print("in FormViewB")  # Output to console
        return super(FormViewB, self).form_valid(form)  # Call the parent's form_valid
