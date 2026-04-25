
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
        form.save()
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Additional logic for FormViewB
        form.save()
        print("in FormViewB")
        return super(FormViewB, self).form_valid(form)
