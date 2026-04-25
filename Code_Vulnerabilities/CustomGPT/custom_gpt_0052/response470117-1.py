
from django.views import generic
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.models import User

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def form_valid(self, form):
        # Check if the user is authenticated
        if self.request.user.is_authenticated:
            return redirect('home')

        # Proceed with the registration logic
        response = super().form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])

        if user is not None:
            login(self.request, user)

        return response

    def form_invalid(self, form):
        # Handle the case when the form is invalid
        return self.render_to_response({'form': form})
