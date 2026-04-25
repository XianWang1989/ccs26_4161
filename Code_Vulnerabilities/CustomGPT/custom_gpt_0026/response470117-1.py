
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # Check if the user is already logged in
            return redirect('home')  # Redirect to home if logged in
        return super().dispatch(request, *args, **kwargs)  # Otherwise, continue with normal flow

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        login(self.request, user)
        return response
