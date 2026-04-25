
# views.py
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        # Redirect to your custom profile redirect view
        return '/redirect/'

# urls.py
urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]
