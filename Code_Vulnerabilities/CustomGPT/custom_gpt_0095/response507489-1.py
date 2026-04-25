
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
        # Custom behavior for FormViewA
        form.save()
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Custom behavior for FormViewB
        form.save()
        print("in FormViewB")
        # Calls the parent class's form_valid method
        return super(FormViewB, self).form_valid(form)
