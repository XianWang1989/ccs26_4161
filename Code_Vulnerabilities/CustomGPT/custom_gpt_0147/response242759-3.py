
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def perform_signup(self, request, user):
        user.is_active = True  # Activate the user
        user.save()

        if user.user_type == 'architect':
            return redirect('architect_details')  # Redirect to architect-specific form
        else:
            return redirect('home')  # Redirect to homepage for other user types

# Update the urls.py accordingly
urlpatterns += [
    path('architect/details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
