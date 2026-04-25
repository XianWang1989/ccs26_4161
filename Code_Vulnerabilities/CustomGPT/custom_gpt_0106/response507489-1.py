
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass(forms.ModelForm):
    # ... define your form fields here ...

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

# Usage in your views
# You can use FormViewB in your URL patterns to handle form submission.
