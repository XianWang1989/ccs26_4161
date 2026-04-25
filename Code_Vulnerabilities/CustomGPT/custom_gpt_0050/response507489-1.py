
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass:
    # Simplified form class - usually a ModelForm
    def save(self):
        pass  # Logic to save the form data

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")
        return super().form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        return super().form_valid(form)

# Usage example in a view
# When FormViewB processes a valid form, the output will be:
# in FormViewB
# in FormViewA
