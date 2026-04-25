
class CustomSignupView(SignupView):
    # other methods...

    def form_valid(self, form):
        response = super().form_valid(form)
        user_type = form.cleaned_data.get('user_type')

        if user_type == 'Architect':
            return redirect('architect_details')
        return response
