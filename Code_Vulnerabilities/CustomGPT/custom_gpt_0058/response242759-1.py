
# yourapp/forms.py
from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('architect', 'Architect'),
        ('other_type', 'Other Type'),
    ])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Automatically activate the user
        user.is_active = True
        user.save()
        return user

# yourapp/views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def additional_info(request):
    if request.method == 'POST':
        # Process the additional info form here
        # Example: Getting business details
        business_details = request.POST.get('business_details')
        # Save details to the user model or elsewhere
        return redirect(reverse('home'))

    return render(request, 'yourapp/additional_info.html')

# yourapp/urls.py
from django.urls import path
from .views import additional_info

urlpatterns = [
    path('additional-info/', additional_info, name='additional_info'),
]

# settings.py
ACCOUNT_SIGNUP_FORM_CLASS = 'yourapp.forms.CustomSignupForm'
