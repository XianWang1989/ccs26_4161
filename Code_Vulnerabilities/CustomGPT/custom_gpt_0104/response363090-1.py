
REQUEST_TYPE_ENTRANCE = '1'  # Ensure this is a string for LIKE comparisons
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__contains=REQUEST_TYPE_ENTRANCE
)
