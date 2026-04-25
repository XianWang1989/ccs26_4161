
REQUEST_TYPE_ENTRANCE = 1
# Translate your regex pattern to LIKE pattern
LIKE_ENTRANCE = '%,{0},%'.format(REQUEST_TYPE_ENTRANCE)  # Example for a middle placement; adjust as necessary.

# Using LIKE instead of REGEXP
entrance_registers = EntranceRegister.objects.filter(authorized_requests__icontains=REQUEST_TYPE_ENTRANCE)
