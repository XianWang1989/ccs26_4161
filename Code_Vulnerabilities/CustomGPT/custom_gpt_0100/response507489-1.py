
from django.views.generic.edit import FormView
from django.urls import reverse

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):  # Called when the form is valid
        form.save()
        print("in FormViewA")  # Output this line
        return super(FormViewA, self).form_valid(form)  # Calls the parent class method

class FormViewB(FormViewA):  # Inherits from FormViewA
    def form_valid(self, form):  # Override the form_valid method
        form.save()
        print("in FormViewB")  # Output this line
        return super(FormViewB, self).form_valid(form)  # Calls FormViewA's form_valid method
