
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass:
    # Assume this is your form class
    pass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # This will print when form_valid is called
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # This will print when form_valid is called for FormViewB
        return super(FormViewB, self).form_valid(form)
