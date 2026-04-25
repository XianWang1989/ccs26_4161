
if request.POST:
    ...
    response['pk-user'] = rental.slug  # Ensure this is set correctly
    return response
