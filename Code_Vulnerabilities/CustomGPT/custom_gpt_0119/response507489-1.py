
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
        form.save()  # Saving the form
        print("in FormViewA")  # Output for debugging
        return super().form_valid(form)  # Call the parent method

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Saving the form again (if necessary)
        print("in FormViewB")  # Output for debugging
        return super().form_valid(form)  # Call the parent method

# In your template, use FormViewB to display the form.
