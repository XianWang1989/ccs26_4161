
# adapters.py (continued)
from django.urls import reverse

class MyAccountAdapter(DefaultAccountAdapter):
    # ... existing code

    def get_login_redirect_url(self, request):
        user_type = request.user.user_type
        if user_type == 'architect':
            return reverse('architect_detail')  # Replace with your desired URL
        return super(MyAccountAdapter, self).get_login_redirect_url(request)
