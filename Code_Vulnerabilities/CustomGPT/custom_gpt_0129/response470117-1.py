
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from . import forms  # Assuming you have forms defined in your forms module
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is already logged in
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to home if user is authenticated
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        login(self.request, user)
        return response
