
REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE},'
).union(
    EntranceRegister.objects.filter(authorized_requests__icontains=f'{REQUEST_TYPE_ENTRANCE},')
).union(
    EntranceRegister.objects.filter(authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE}')
).union(
    EntranceRegister.objects.filter(authorized_requests__exact=str(REQUEST_TYPE_ENTRANCE))
)
