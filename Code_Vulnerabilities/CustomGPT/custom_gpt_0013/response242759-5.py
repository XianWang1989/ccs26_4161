
from allauth.account.utils import complete_signup

class CustomSignupView(SignupView):
    def perform_signup(self, request, user):
        user.is_active = True
        user.save()

        user_type = self.request.POST.get('user_type')
        if user_type == 'architect':
            return redirect('architect_details')
        else:
            return complete_signup(request, user, self.get_success_url())

# In your urls.py
path('architect/details/', ArchitectDetailsView.as_view(), name='architect_details'),
