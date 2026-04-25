
# forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import UserProfile

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('other', 'Other')])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = True  # Automatically activate user
        user.save()

        user_profile = UserProfile(user=user)
        user_profile.user_type = self.cleaned_data['user_type']
        user_profile.save()

        return user

# views.py
from allauth.account.views import SignupView
from .forms import CustomSignupForm

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def get_success_url(self):
        user_type = self.request.POST.get('user_type')
        if user_type == 'architect':
            return '/business-details/'  # Redirect to business details form
        return super().get_success_url()

# url_patterns.py
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]

# models.py (you may already have this model)
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50)
