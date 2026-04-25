
# Inside EditSpaceView after saving the rental object.
response['pk-user'] = rental.slug  # Make sure 'rental.slug' is defined and not None
return response
