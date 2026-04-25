
# views.py
from django.shortcuts import redirect
from django.views import View

class PostSignupView(View):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == 'architect':
            return redirect('business_details_form')  # Replace with actual view name
        return super().dispatch(request, *args, **kwargs)

# In your urls.py
from django.urls import path
from .views import PostSignupView

urlpatterns = [
    path('accounts/signup/', PostSignupView.as_view(), name='signup'),
    # Other paths...
]
