
# views.py
from allauth.account.views import SignupView
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('arch', 'Architect'), ('client', 'Client')])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user

class CustomSignupView(SignupView):
    def get_success_url(self):
        user_type = self.request.POST.get('user_type')
        if user_type == 'arch':
            return '/business-details-form/'
        return super().get_success_url()

@receiver(user_signed_up)
def activate_user(request, user, **kwargs):
    user.is_active = True
    user.save()
