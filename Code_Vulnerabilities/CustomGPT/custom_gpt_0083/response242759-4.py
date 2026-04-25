
def save(self, request):
    user = super(CustomSignupForm, self).save(request)
    user.is_active = True
    user.save()

    if self.cleaned_data['user_type'] == 'Architect':
        # Redirect to additional info page
        request.session['user_type'] = 'Architect'  # Store user type
        return redirect('additional_info')

    return user
