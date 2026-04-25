
# views.py
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponseRedirect

class UserTypeRedirectView(View):
    def get(self, request):
        user_type = request.user.user_type
        if user_type == 'Architect':
            return redirect('architect_details')  # Your url pattern for details
        return redirect('home')  # Default redirect

# urls.py
from django.urls import path
from .views import UserTypeRedirectView

urlpatterns = [
    # Other url patterns
    path('redirect/', UserTypeRedirectView.as_view(), name='user_type_redirect'),
]

# Make sure to call this view after login
