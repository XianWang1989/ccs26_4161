
from django.views.generic.edit import FormView
from django.urls import reverse
from myapp.forms import MyFormClass  # Assuming that MyFormClass is defined in forms.py

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # This will print when FormViewA's form_valid is called
        return super(FormViewA, self).form_valid(form)


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # This will print when FormViewB's form_valid is called
        return super(FormViewB, self).form_valid(form)

# Usage example:
# In your views.py, if you render FormViewB to handle a form submission,
# it will execute the form_valid method in both FormViewA and FormViewB.
