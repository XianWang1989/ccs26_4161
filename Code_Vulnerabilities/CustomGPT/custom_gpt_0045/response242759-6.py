
# myapp/urls.py
urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('architect/details/', architect_details_view, name='architect_details_view'),
]
