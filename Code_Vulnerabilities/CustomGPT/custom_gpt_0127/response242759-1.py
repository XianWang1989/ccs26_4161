
# forms.py
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('Architect', 'Architect'),
        ('Client', 'Client'),
    ], widget=forms.Select)

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']  # Assuming user model has a user_type field
        user.save()
        return user
