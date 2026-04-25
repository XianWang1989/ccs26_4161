
REQUEST_TYPE_ENTRANCE = '1'
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=REQUEST_TYPE_ENTRANCE
).filter(
    Q(authorized_requests__startswith=REQUEST_TYPE_ENTRANCE + ',') |
    Q(authorized_requests__endswith=',' + REQUEST_TYPE_ENTRANCE) |
    Q(authorized_requests=REQUEST_TYPE_ENTRANCE)
)
