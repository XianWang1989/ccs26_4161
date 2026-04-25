
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
        print("in FormViewA")  # Output from FormViewA
        return super(FormViewA, self).form_valid(form)


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Additional behavior for FormViewB
        print("in FormViewB")  # Output from FormViewB
        return super(FormViewB, self).form_valid(form)  # Calls FormViewA's form_valid
