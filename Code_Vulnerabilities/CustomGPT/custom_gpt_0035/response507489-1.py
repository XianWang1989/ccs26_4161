
from django.views.generic.edit import FormView
from django.urls import reverse

# Parent form view
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # Save the form instance
        form.save()
        print("in FormViewA")  # This prints when FormViewA's form_valid is called
        return super(FormViewA, self).form_valid(form)  # Calls the parent form_valid

# Child form view
class FormViewB(FormViewA):
    def form_valid(self, form):
        # Save the form instance in the child view
        form.save()
        print("in FormViewB")  # This prints when FormViewB's form_valid is called
        return super(FormViewB, self).form_valid(form)  # Calls FormViewA's form_valid
