
REQUEST_TYPE_ENTRANCE = '1'
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=REQUEST_TYPE_ENTRANCE
)
