
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('user', 'User'), ('architect', 'Architect')])

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
