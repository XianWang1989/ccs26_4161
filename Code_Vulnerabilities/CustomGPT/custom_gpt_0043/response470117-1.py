
class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('platforms')

    def form_valid(self, form):
        # Check if the user is already authenticated
        if self.request.user.is_authenticated:
            return redirect('home')  # Redirect to home if user is already logged in

        # If user is not authenticated, proceed with the normal registration
        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.instance.username, password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        return response
