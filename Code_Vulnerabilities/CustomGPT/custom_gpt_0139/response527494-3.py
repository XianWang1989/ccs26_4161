
def send_message(request, user_id):
    if request.method == 'POST':
        message_content = request.POST.get('message')
        # Logic to save the message
        postman_views.send_message(request.user, user_id, message_content)
        return redirect('postman:inbox')
    else:
        return redirect('postman:send', user_id=user_id)
