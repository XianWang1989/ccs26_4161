
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('architect', 'Architect'),
        ('engineer', 'Engineer'),
        # Add other user types
    ])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']  # Assuming you have a field in your User model
        user.save()
        return user
