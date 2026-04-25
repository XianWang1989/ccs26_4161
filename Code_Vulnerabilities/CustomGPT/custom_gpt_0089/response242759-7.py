
# yourapp/views.py (continuation)
def signup_redirect(request):
    if request.user.is_authenticated and request.session.get('business_details_required'):
        return redirect('business_details')
    return redirect('default_redirect_url')
