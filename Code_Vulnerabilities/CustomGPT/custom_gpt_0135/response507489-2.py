
from django.views.generic.edit import FormView
from django.urls import reverse
from myapp.forms import MyFormClass  # Ensure you have this form defined

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def form_valid(self, form):
        form.save()
        print("in FormViewA")
        return super().form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        print("in FormViewB")
        return super().form_valid(form)  # Calls FormViewA's form_valid
