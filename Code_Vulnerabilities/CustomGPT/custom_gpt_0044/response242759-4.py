
def get_success_url(self):
    self.request.user.is_active = True
    self.request.user.save()

    user_type = self.request.user.user_type
    if user_type == 'Architect':
        return reverse('architect_business_details')

    return super().get_success_url()
