
# views.py
from django.urls import reverse
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        if user.user_type == 'architect':
            return redirect(reverse('architect_details'))
        return super().form_valid(form)

# Update your URLs
# urls.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect-details/', architect_details_view, name='architect_details'),
]
