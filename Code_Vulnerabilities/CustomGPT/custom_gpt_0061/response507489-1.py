
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass:
    # Your form definition goes here
    pass

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Perform actions on valid form
        form.save()
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Custom behavior in FormViewB
        form.save()
        print("in FormViewB")
        return super(FormViewB, self).form_valid(form)

# Usage in a Django template would call FormViewB
