
# Assuming REQUEST_TYPE_ENTRANCE is defined as 1
REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE},'
).union(
    EntranceRegister.objects.filter(authorized_requests__istartswith=f'{REQUEST_TYPE_ENTRANCE},')
).union(
    EntranceRegister.objects.filter(authorized_requests__iendswith=f',{REQUEST_TYPE_ENTRANCE}')
).union(
    EntranceRegister.objects.filter(authorized_requests__exact=str(REQUEST_TYPE_ENTRANCE))
)
