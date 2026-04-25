
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Handles the form saving logic
        print("in FormViewA")
        return super().form_valid(form)  # Calls parent class's form_valid

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Can include additional logic if needed
        print("in FormViewB")
        return super().form_valid(form)  # Calls FormViewA's form_valid
