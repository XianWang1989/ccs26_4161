
REQUEST_TYPE_ENTRANCE = 1

# Adjusting the pattern for SQLite using LIKE
pattern = '%{},%'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.filter(authorized_requests__icontains=REQUEST_TYPE_ENTRANCE)

# If you're checking specifically for edge cases (start, middle, end)
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__startswith='{}'.format(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests__endswith='{}'.format(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests__icontains=',{}'.format(REQUEST_TYPE_ENTRANCE))
)

# Displaying the SQL query for debugging
print(entrance_registers.query)
