
from django.views.generic.edit import FormView
from django.urls import reverse
from myapp.forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form instance
        print("in FormViewA")  # Output from FormViewA
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form instance in FormViewB
        print("in FormViewB")  # Output from FormViewB
        return super(FormViewB, self).form_valid(form)  # Call FormViewA's form_valid

# Use FormViewB in your URL configuration or template
