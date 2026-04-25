
from django.shortcuts import redirect

class CustomSignupForm(SignupForm):
    #... (previous code)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        if user.user_type == 'architect':
            # Redirect to business details form
            return redirect('business_details')
        return user
