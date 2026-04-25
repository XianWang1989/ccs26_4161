
from django.views.generic.edit import FormView
from django.urls import reverse

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form
        print("in FormViewA")  # Output specific to FormViewA
        return super(FormViewA, self).form_valid(form)  # Call the parent method

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form again (if needed)
        print("in FormViewB")  # Output specific to FormViewB
        return super(FormViewB, self).form_valid(form)  # Call FormViewA's form_valid
