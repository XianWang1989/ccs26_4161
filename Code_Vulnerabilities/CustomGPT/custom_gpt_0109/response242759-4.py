
# yourapp/views.py
from django.shortcuts import redirect
from django.views import View

class UserTypeRedirectView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.user_type == 'architect':
                return redirect('architect_details_page')  # Your specific URL
            elif user.user_type == 'designer':
                return redirect('designer_details_page')
        return super().get(request, *args, **kwargs)
