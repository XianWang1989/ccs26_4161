
# forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ('Architect', 'Architect'),
        ('Engineer', 'Engineer'),
        ('Client', 'Client'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']  # Save user type
        user.save()
        return user

# In your settings.py
ACCOUNT_SIGNUP_FORM_CLASS = 'yourapp.forms.CustomSignupForm'
