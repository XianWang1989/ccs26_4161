
# myapp/forms.py
from django.urls import reverse
from django.shortcuts import redirect

class CustomSignupForm(SignupForm):
    # ... [previous code]

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        # Redirect to business details if user type is Architect
        if user.user_type == 'Architect':
            return redirect(reverse('business_details'))

        return user
