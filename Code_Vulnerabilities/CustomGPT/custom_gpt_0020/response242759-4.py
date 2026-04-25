
class CustomSignupView(SignupView):
    # ... (previous code)

    def get_success_url(self):
        user_type = self.request.POST.get('user_type')
        if user_type == 'architect':
            return reverse('architect_details')  # URL for additional form
        return super().get_success_url()
