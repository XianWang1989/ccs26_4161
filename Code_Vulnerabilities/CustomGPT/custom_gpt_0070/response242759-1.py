
# views.py
from allauth.account.views import SignupView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if response.status_code == 302:
            user = self.get_user(request)
            if user:
                user.is_active = True
                user.save()
        return response

    def get_user(self, request):
        email = request.POST.get('email')
        return User.objects.filter(email=email).first()
