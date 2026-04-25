
from django.views.generic.edit import FormView
from myapp.forms import MyFormClass
from django.urls import reverse

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # This will run
        return super().form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # This will run
        return super().form_valid(form)

# When FormViewB is used to process a form submission:
# Output:
# in FormViewB
# in FormViewA
