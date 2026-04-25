
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import MyFormClass  # Assuming this is your form

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("In FormViewA")
        return super(FormViewA, self).form_valid(form)


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("In FormViewB")
        return super(FormViewB, self).form_valid(form)
