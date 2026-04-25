
from django.views.generic.edit import FormView
from django.urls import reverse

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)  # Calls parent method

class FormViewB(FormViewA):
    def form_valid(self, form):
        # This method overrides the parent method
        form.save()
        print("in FormViewB")
        return super(FormViewB, self).form_valid(form)  # Calls FormViewA's method

