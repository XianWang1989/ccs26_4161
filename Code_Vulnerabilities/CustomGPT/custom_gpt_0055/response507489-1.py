
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass  # Assume you have a form class defined

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")
        return super().form_valid(form)  # Calls FormView's form_valid

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        return super().form_valid(form)  # Calls FormViewA's form_valid
