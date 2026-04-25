
# forms.py (continue)

from allauth.account.utils import complete_signup

class CustomSignupForm(SignupForm):

    # ... [as before] ...

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        # Redirect based on user type after signup
        complete_signup(request, user, 'yourapp:user_type_redirect')  # URL name of your redirect view

        return user
