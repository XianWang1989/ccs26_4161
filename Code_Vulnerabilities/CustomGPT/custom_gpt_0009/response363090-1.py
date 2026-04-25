
REQUEST_TYPE_ENTRANCE = 1
# Using LIKE for SQLite
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__contains=str(REQUEST_TYPE_ENTRANCE)
)
