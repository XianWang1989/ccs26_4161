
# Before executing your queries
if request.is_local:
    settings.logging = True  # Modify settings as needed for debugging
else:
    settings.logging = False
