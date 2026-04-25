
from django.views.generic.edit import FormView
from django.urls import reverse
from myapp.forms import MyFormClass  # Assuming you have a form class defined

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form data
        print("in FormViewA")
        # Call the parent class's form_valid to handle the success URL redirection
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form data again
        print("in FormViewB")
        # Call the parent class's form_valid to continue the success processing
        return super(FormViewB, self).form_valid(form)

# When you instantiate FormViewB in your Django project,
# the output will be:
# in FormViewB
# in FormViewA
