
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass(forms.Form):
    # Define your form fields here
    field_name = forms.CharField()

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Custom logic for FormViewA
        form.save()
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)


class FormViewB(FormViewA):
    def form_valid(self, form):
        # Custom logic specific to FormViewB
        print("in FormViewB")
        return super(FormViewB, self).form_valid(form)
