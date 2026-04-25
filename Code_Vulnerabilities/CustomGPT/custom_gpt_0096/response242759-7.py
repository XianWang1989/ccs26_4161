
urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('additional-info/', AdditionalInfoView.as_view(), name='additional_info'),
]
