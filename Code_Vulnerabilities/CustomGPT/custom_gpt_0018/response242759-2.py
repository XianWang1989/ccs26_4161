
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('Architect', 'Architect'), ('Engineer', 'Engineer')])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']  # Assuming you have a user_type field on your User model
        user.save()
        return user
