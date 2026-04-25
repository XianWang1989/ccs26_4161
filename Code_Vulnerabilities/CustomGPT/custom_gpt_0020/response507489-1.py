
from django.views.generic.edit import FormView
from django.urls import reverse
from myapp.forms import MyFormClass  # Assuming you have a form class defined

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Save the form
        print("in FormViewA")  # Output specific to FormViewA
        return super(FormViewA, self).form_valid(form)  # Call the parent's form_valid

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Save the form again
        print("in FormViewB")  # Output specific to FormViewB
        return super(FormViewB, self).form_valid(form)  # Call the parent's form_valid (FormViewA)

# Example of usage in a urls.py configuration
from django.urls import path
from myapp.views import FormViewB

urlpatterns = [
    path('my-form/', FormViewB.as_view(), name='my_form_view'),
]
