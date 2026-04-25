
# forms.py
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_type_choices = [
        ('architect', 'Architect'),
        ('client', 'Client'),
    ]
    user_type = forms.ChoiceField(choices=user_type_choices)

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
