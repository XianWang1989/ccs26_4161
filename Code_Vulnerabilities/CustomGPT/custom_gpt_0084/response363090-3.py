
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE)
)
