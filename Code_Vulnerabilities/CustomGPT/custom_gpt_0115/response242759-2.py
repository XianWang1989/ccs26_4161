
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ('Architect', 'Architect'),
        ('Client', 'Client'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
