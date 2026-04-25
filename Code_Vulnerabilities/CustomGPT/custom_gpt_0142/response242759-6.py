
# views.py
from django.shortcuts import redirect
from allauth.account.utils import complete_signup

class CustomSignupView(CreateView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        self.object = form.save(self.request)
        user_type = form.cleaned_data.get('user_type')

        if user_type == 'architect':
            return redirect('business_details')  # Redirect to the additional details page
        else:
            return complete_signup(self.request, self.object, 'yourapp:next_step_url')  # Default next step
