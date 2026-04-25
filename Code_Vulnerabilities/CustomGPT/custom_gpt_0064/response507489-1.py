
from django.views.generic.edit import FormView
from django.urls import reverse
from myapp.forms import MyFormClass  # Adjust as necessary

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # This will run when form_valid is called
        return super(FormViewA, self).form_valid(form)


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # This runs first
        return super(FormViewB, self).form_valid(form)  # Calls FormViewA's form_valid
