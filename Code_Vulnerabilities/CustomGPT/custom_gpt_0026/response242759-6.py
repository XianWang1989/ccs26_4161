
def form_valid(self, form):
    user = super().form_valid(form)
    user.is_active = True
    user.save()

    if user.user_type == 'architect':
        return redirect('architect_details')

    return super().form_valid(form)
