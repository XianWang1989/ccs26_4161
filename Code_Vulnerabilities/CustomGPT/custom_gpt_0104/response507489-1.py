
from django.views.generic.edit import FormView
from django.urls import reverse
from myapp.forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Logic for FormViewA
        form.save()
        print("in FormViewA")
        # Call the parent form_valid to continue the process
        return super(FormViewA, self).form_valid(form)


class FormViewB(FormViewA):
    def form_valid(self, form):
        # Logic for FormViewB
        form.save()
        print("in FormViewB")
        # Call FormViewA's form_valid method
        return super(FormViewB, self).form_valid(form)

# Example usage in your views.py
# You would usually register these views in your urls.py
