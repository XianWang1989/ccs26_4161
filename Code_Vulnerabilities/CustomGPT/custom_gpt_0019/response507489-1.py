
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
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        # Still calling the parent method
        return super(FormViewB, self).form_valid(form)

# In your template, when using FormViewB:
# It will trigger:
# > in FormViewB
# > in FormViewA
