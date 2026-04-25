
REQUEST_TYPE_ENTRANCE = 1
# Create a LIKE pattern
LIKE_PATTERN = f'%{REQUEST_TYPE_ENTRANCE}%'

# Use filtering with LIKE
entrance_registers = EntranceRegister.objects.filter(authorized_requests__icontains=REQUEST_TYPE_ENTRANCE)
