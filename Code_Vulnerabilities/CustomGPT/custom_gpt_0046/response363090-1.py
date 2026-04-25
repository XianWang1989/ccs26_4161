
REQUEST_TYPE_ENTRANCE = '1'
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE},'
).union(
    EntranceRegister.objects.filter(
        authorized_requests__startswith=f'{REQUEST_TYPE_ENTRANCE},'
    )
).union(
    EntranceRegister.objects.filter(
        authorized_requests__endswith=f',{REQUEST_TYPE_ENTRANCE}'
    )
).union(
    EntranceRegister.objects.filter(
        authorized_requests=REQUEST_TYPE_ENTRANCE
    )
)
