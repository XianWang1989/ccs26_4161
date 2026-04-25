
# adapters.py (continuation)
def complete_signup(self, request, user, login):
    response = super().complete_signup(request, user, login)
    return post_signup_redirect(request)
