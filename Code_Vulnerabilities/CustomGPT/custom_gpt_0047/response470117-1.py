
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
        # Check if the user is already logged in
        if self.request.user.is_authenticated:
            return redirect('home')  # Redirect to home if user is already authenticated

        # Proceed with registration logic
        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        login(self.request, user)
        return response

    def form_invalid(self, form):
        # If the form is invalid, you might want to render the registration template again
        return self.render_to_response({'form': form})
