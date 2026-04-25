
# views.py
class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        user.is_active = True
        user.save()

        user_type = form.cleaned_data['user_type']
        if user_type == 'architect':
            return redirect('architect_details')  # Redirect to the additional details form

        return complete_signup(self.request, user)
