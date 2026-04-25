
# forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('other', 'Other')], required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
