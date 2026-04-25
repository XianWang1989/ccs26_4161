
# forms.py
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('Architect', 'Architect'), ('Client', 'Client')])

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
