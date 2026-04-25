
def save(self, request):
    user = super(CustomSignupForm, self).save(request)
    user.is_active = True
    user.save()

    # Redirect to additional info if user type is 'architect'
    if self.cleaned_data['user_type'] == 'architect':
        return redirect(reverse('additional_info'))

    return user
