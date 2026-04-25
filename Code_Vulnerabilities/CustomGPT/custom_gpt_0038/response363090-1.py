
REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__contains=f',{REQUEST_TYPE_ENTRANCE},'
).union(
    EntranceRegister.objects.filter(
        authorized_requests__startswith=f'{REQUEST_TYPE_ENTRANCE},'
    ),
    EntranceRegister.objects.filter(
        authorized_requests__endswith=f',{REQUEST_TYPE_ENTRANCE}'
    ),
    EntranceRegister.objects.filter(
        authorized_requests=f'{REQUEST_TYPE_ENTRANCE}'
    )
)
