
# myapp/forms.py
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(
        choices=(('Architect', 'Architect'), ('Designer', 'Designer')),
        label="User Type"
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']  # Make sure to have a field user_type in your User model
        user.save()
        return user
