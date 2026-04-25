
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from . import forms  # Make sure to adjust this import according to your project structure
from .models import User  # Ensure the User model is correctly imported

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        if user is not None:  # Check if the user is authenticated
            login(self.request, user)
        return response
