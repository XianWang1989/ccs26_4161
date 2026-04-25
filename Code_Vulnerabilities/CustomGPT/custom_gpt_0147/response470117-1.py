
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views import generic
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
            return redirect('home')  # Change 'home' to the desired redirect URL

        # If not authenticated, proceed with registration
        response = super(RegisterView, self).form_valid(form)
        # Authenticate and log the user in
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        return response
