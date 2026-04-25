
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from . import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def form_valid(self, form):
        # Check if the user is already logged in
        if self.request.user.is_authenticated:
            return redirect('home')  # Redirect to home if user is already authenticated

        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])

        if user is not None:
            login(self.request, user)  # Log the user in if authentication is successful

        return response
