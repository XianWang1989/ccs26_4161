
from django.views.generic.edit import FormView
from django.urls import reverse

class BaseFormView(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("BaseFormView")
        return super(BaseFormView, self).form_valid(form)

class DerivedFormView(BaseFormView):
    def form_valid(self, form):
        form.save()
        print("DerivedFormView")
        return super(DerivedFormView, self).form_valid(form)

# Usage:
# When you use DerivedFormView, both print statements will trigger:
# - "DerivedFormView"
# - "BaseFormView"
