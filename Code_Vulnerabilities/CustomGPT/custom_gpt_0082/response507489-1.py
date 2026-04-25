
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass(forms.Form):
    # Define your form fields here
    name = forms.CharField(max_length=100)

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Logic to execute when the form is valid
        print("In FormViewA")
        return super().form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Additional logic specific to FormViewB
        print("In FormViewB")
        return super().form_valid(form)

# In your template, if you use FormViewB,
# both "In FormViewB" and "In FormViewA" will be printed upon form submission.
