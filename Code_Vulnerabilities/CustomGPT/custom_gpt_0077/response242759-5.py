
# views.py
from django.shortcuts import redirect
from django.views import View

class UserTypeSelectView(View):
    def post(self, request, *args, **kwargs):
        user_type = request.POST.get('user_type')
        request.session['user_type'] = user_type

        if user_type == 'architect':
            return redirect('architect_details')
        # Redirect to a different form for other user types if needed

        return redirect('home')

class ArchitectDetailsView(View):
    def get(self, request, *args, **kwargs):
        # Render form for business details here
        pass

    def post(self, request, *args, **kwargs):
        # Handle saving business details here
        pass
