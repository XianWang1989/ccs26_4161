
# forms.py
from allauth.account.adapter import get_adapter
from allauth.account.utils import complete_signup
from django import forms
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSignupForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('other', 'Other')])

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'user_type')

    def save(self, request):
        user = super().save(commit=False)
        user.is_active = True  # Activate user upon signup
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
