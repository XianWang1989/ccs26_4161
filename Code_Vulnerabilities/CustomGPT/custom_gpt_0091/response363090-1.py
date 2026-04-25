
REQUEST_TYPE_ENTRANCE = 1

# Constructing the pattern for SQLite LIKE queries
pattern_entrance = '{0},%,%,{0},%,%,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Adjusting the query to use LIKE instead of regex
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE)
)

# You might need to adapt the LIKE logic depending on your specific needs
