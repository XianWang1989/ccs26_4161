
urlpatterns = [
    ...
    path('postman/send/<str:recipient_username>/', send_message_view, name='send_message'),
]
