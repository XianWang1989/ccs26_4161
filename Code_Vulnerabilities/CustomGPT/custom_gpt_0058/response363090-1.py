
REQUEST_TYPE_ENTRANCE = '1'  # Ensuring it is a string for LIKE
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=',' + REQUEST_TYPE_ENTRANCE + ','  # Match the pattern with LIKE
).union(
    EntranceRegister.objects.filter(authorized_requests__startswith=REQUEST_TYPE_ENTRANCE + ',')
).union(
    EntranceRegister.objects.filter(authorized_requests__endswith=(',' + REQUEST_TYPE_ENTRANCE))
).union(
    EntranceRegister.objects.filter(authorized_requests=REQUEST_TYPE_ENTRANCE)
)
