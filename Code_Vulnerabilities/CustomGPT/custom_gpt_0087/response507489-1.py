
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # Output when FormViewA's method is called
        return super().form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # Output when FormViewB's method is called
        return super().form_valid(form)
