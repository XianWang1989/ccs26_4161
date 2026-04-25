
# forms.py (Add logic in the save method)
from django.urls import reverse

class CustomSignupForm(SignupForm):
    # same as above

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        # Handle redirection based on user type
        if user.user_type == 'architect':
            return redirect(reverse('business_details'))  # Name of your detail view
        else:
            return user
