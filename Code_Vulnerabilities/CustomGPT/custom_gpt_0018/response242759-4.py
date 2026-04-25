
class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.POST.get('user_type')
        if user_type == 'Architect':
            return '/architect-details/'  # Redirect to business details form
        return super().get_success_url()
