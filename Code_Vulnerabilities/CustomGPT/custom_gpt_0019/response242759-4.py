
# views.py (add to CustomSignupView)
def get_success_url(self):
    if self.request.user.user_type == 'arch':
        return '/architect-details/'  # Redirect to architect details form
    return super().get_success_url()
