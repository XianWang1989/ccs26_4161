
# yourapp/forms.py (continuation)
from django.contrib import messages

class CustomSignupForm(SignupForm):
    # ... [existing code]

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        if user.user_type == 'architect':
            messages.success(request, 'Please fill out your business details.')
            request.session['business_details_required'] = True

        return user
