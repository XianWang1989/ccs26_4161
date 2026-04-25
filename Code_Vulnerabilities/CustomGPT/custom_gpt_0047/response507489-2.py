
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # First, save the form data in this view.
        form.save()
        print("in FormViewA")
        # Call the parent's form_valid to continue the process.
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Save the form data in this derived view.
        form.save()
        print("in FormViewB")
        # Call the parent's form_valid to ensure the flow continues.
        return super(FormViewB, self).form_valid(form)
