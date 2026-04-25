
from django.urls import path
from django.views.generic.edit import FormView
from django import forms
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

# Define a simple form
class MyFormClass(forms.Form):
    name = forms.CharField(max_length=100)

# Base view class
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('success_url')  # Redirect after submission

    def form_valid(self, form):
        # Logic to be executed upon valid form submission
        form.save()  # Assuming a model form 
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)

# Subclass that overrides form_valid
class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()  # Logic specific to FormViewB
        print("in FormViewB")
        return super(FormViewB, self).form_valid(form)

# URL patterns to wire up the views
urlpatterns = [
    path('form-a/', FormViewA.as_view(), name='form-a'),
    path('form-b/', FormViewB.as_view(), name='form-b'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success_url'),
]
