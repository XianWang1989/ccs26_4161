
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('Architect', 'Architect'), ('Other', 'Other')])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Automatically activate the user
        user.is_active = True
        user.save()
        return user
