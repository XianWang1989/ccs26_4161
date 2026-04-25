
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    # Existing code...

    def form_valid(self, form):
        response = super().form_valid(form)

        # Activate the user
        self.user.is_active = True
        self.user.save()

        # Redirect to step two if user type is 'Architect'
        if form.cleaned_data['user_type'] == 'architect':
            return redirect('architect_details_url')  # Replace with your URL name

        return response
