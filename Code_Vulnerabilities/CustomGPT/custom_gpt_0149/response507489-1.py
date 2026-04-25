
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
        print("in FormViewA")
        return super().form_valid(form)  # Python 3 syntax

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        return super().form_valid(form)  # Calls FormViewA's form_valid
