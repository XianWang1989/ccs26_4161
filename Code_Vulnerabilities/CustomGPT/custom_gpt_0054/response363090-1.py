
REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__contains=str(REQUEST_TYPE_ENTRANCE)  # Matches anywhere in the string
)
