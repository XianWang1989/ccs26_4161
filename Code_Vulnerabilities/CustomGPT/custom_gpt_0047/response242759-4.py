
# signals.py
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    user_type = request.POST.get('user_type')
    if user_type == 'architect':
        return redirect('additional_info')
