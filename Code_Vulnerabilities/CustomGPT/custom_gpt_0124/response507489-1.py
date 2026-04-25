
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass(forms.Form):
    # Define your form fields here
    pass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Save the form
        form.save()
        print("in FormViewA")
        # Call the parent class's form_valid
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Save the form
        form.save()
        print("in FormViewB")
        # Call FormViewA's form_valid method
        return super(FormViewB, self).form_valid(form)

# Usage
# When you use FormViewB it will print both messages like this:
# in FormViewB
# in FormViewA
