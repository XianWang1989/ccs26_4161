
# forms.py (continued)
from django.urls import reverse

class CustomSignupForm(SignupForm):
    # ... existing code ...

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return redirect(reverse('check_user_type'))
