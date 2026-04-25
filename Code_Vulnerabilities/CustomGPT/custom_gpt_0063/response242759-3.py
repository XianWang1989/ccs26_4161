
class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        user.is_active = True
        user.save()

        user_type = form.cleaned_data['user_type']
        if user_type == 'architect':
            return redirect('architect_business_details')  # Redirect to the business details page
        return super().form_valid(form)
