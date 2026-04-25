
# views.py
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user_type = form.cleaned_data.get('user_type')

        if user_type == 'architect':
            # Store in session and redirect
            self.request.session['user_type'] = 'architect'
            return redirect('your_business_details_view')

        return response
