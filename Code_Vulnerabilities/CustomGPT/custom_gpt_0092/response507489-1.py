
from django.urls import reverse
from django.views.generic.edit import FormView

# The first FormView that handles form processing
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Save the form data
        form.save()
        print("in FormViewA")  # Output from FormViewA
        return super(FormViewA, self).form_valid(form)

# The second FormView that inherits from FormViewA
class FormViewB(FormViewA):
    def form_valid(self, form):
        # Save the form data again (if necessary)
        form.save()
        print("in FormViewB")  # Output from FormViewB
        return super(FormViewB, self).form_valid(form)  # Calls the parent method
