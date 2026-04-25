
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .models import User  # Adjust the import as necessary
from . import forms  # Make sure to import your forms

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect authenticated users to home page
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        return response
