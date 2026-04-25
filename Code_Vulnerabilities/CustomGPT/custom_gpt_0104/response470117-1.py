
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def form_valid(self, form):
        # Check if the user is already logged in
        if self.request.user.is_authenticated:
            return redirect('home')  # Redirect to home if user is authenticated

        # Call the superclass's form_valid method to handle the registration logic
        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        login(self.request, user)
        return response
