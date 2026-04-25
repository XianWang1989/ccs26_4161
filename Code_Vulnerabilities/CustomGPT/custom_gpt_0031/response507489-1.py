
from django.views.generic.edit import FormView
from django.urls import reverse

class MyFormClass(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'

class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()  # Saving the form data to the database
        print("in FormViewA")  # Debug output
        return super(FormViewA, self).form_valid(form)  # Call the parent method

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Saving the form data again (optional redundancy)
        print("in FormViewB")  # Debug output
        return super(FormViewB, self).form_valid(form)  # Call the parent method
