
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass:
    # Your form class implementation
    pass

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

# When FormViewB is used:
# Output:
# in FormViewB
# in FormViewA
