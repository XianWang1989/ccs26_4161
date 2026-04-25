
from django.views.generic.edit import FormView
from django.urls import reverse
from myapp.forms import MyFormClass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Assuming there's a save method in your form
        form.save()
        print("in FormViewA")
        return super().form_valid(form)  # Call the parent form_valid

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        return super().form_valid(form)  # Call the parent form_valid again
