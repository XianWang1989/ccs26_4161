
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('client', 'Client')])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = True
        user.save()
        return user
