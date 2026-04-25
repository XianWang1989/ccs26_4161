
from allauth.account.forms import SignupForm
from django import forms

class SignupForm(SignupForm):
    user_type = forms.ChoiceField(
        choices=[('Architect', 'Architect'), ('Designer', 'Designer')],
        required=True
    )

    def save(self, request):
        user = super().save(request)
        user.is_active = True  # Automatically activate user
        user.save()
        return user
