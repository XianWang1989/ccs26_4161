
REQUEST_TYPE_ENTRANCE = 1
REQUEST_TYPE_STRING = str(REQUEST_TYPE_ENTRANCE)

# Using contains to simulate a regex-like match
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__contains=f'{REQUEST_TYPE_STRING},'
) | EntranceRegister.objects.filter(
    authorized_requests__contains=fr',{REQUEST_TYPE_STRING},'
) | EntranceRegister.objects.filter(
    authorized_requests__contains=fr',{REQUEST_TYPE_STRING}'
) | EntranceRegister.objects.filter(
    authorized_requests=f'{REQUEST_TYPE_STRING}'
)
