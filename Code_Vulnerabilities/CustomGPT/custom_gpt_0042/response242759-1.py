
# views.py
from allauth.account.views import SignupView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = super().form_valid(form)
        user.is_active = True  # Automatically activate user
        user.save()
        return user
