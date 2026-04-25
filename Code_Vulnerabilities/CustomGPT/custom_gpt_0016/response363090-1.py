
REQUEST_TYPE_ENTRANCE = 1
search_pattern = f'%{REQUEST_TYPE_ENTRANCE}%'

# Using LIKE instead of REGEX for SQLite compatibility
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=REQUEST_TYPE_ENTRANCE
)
