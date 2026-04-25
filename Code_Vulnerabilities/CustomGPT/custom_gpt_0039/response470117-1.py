
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from .models import User
from . import forms

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def form_valid(self, form):
        # Check if the user is already authenticated
        if self.request.user.is_authenticated:
            return redirect('home')  # Redirect to home if user is logged in

        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        login(self.request, user)
        return response

    def get(self, request, *args, **kwargs):
        # Redirect to home if user is authenticated on GET request
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to home if user is logged in
        return super().get(request, *args, **kwargs)
