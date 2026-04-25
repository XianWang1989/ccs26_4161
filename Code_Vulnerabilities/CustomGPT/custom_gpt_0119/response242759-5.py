
from allauth.account.utils import send_email_confirmation

class CustomSignupForm(SignupForm):
    # ... existing code ...

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        # Redirect based on user type
        if user.user_type == 'Architect':
            return 'yourapp:business_details'  # Adjust this to your URL name

        return user
