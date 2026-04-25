
def perform_signup(self, request, user):
    super().perform_signup(request, user)
    if user.user_type == 'architect':
        return redirect('business_details')
