
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ('architect', 'Architect'),
        ('client', 'Client'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
