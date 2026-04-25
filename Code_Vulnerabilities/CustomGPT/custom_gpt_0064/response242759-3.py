
# forms.py
from allauth.account.forms import SignupForm
from django import forms

class MyCustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('architect', 'Architect'),
        ('client', 'Client'),
    ])

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']  # Assuming you have a user_type field on your user model
        user.save()
        return user
