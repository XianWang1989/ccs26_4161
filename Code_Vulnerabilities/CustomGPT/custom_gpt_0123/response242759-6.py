
from allauth.account.utils import complete_signup
from django.urls import reverse

def custom_complete_signup(request, user, current_site, adapter, **kwargs):
    next_url = reverse('architect_details') if user.user_type == 'Architect' else 'home'
    complete_signup(request, user, next_url=next_url)

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False  # Ensure you set this
