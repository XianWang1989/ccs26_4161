
# views.py
from django.shortcuts import redirect

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = super().form_valid(form)
        user.is_active = True
        user.save()

        self.request.session['user_type'] = form.cleaned_data['user_type']

        if user.user_type == 'architect':
            return redirect('architect_details')  # Redirect to architect details form
        return super().get_success_url()

# Architect details view
def architect_details_view(request):
    if request.method == 'POST':
        # handle form submission
        pass
    return render(request, 'architect_details.html')
