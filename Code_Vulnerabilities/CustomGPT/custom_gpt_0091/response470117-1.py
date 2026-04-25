
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from yourapp import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def form_valid(self, form):
        # Check if user is already authenticated
        if self.request.user.is_authenticated:
            return redirect('home')

        # Save the new user
        response = super(RegisterView, self).form_valid(form)

        # Authenticate and log in the user
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)

        return response
