
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from .models import User
from . import forms
from django.urls import reverse_lazy

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def form_valid(self, form):
        # Check if the user is already logged in
        if self.request.user.is_authenticated:
            return redirect('home')

        # If not logged in, continue with the registration logic
        response = super(RegisterView, self).form_valid(form)

        # Authenticate and log in the new user
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        login(self.request, user)
        return response
