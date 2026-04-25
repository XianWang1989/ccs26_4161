
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass  # Assuming you have defined your form class

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form data
        print("in FormViewA")  # Output from FormViewA
        return super(FormViewA, self).form_valid(form)  # Call the parent class's form_valid

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form data
        print("in FormViewB")  # Output from FormViewB
        return super(FormViewB, self).form_valid(form)  # Call the parent class's form_valid
