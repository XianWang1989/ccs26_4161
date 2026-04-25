
# forms.py
from django import forms
from allauth.account.forms import SignupForm

USER_TYPE_CHOICES = [
    ('individual', 'Individual'),
    ('architect', 'Architect'),
]

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
