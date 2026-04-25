
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def form_valid(self, form):
        # Check if the user is already authenticated
        if self.request.user.is_authenticated:
            return redirect('home')

        response = super(RegisterView, self).form_valid(form)

        # Authenticate and login the user
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)

        return response
