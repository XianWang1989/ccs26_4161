
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # This might save to database
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # This might save to database
        print("in FormViewB")
        return super(FormViewB, self).form_valid(form)

# When this view is triggered:
# FormViewB's form_valid is called, then calls FormViewA's form_valid.
