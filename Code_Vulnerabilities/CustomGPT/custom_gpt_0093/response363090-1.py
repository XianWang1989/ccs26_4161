
REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE},') |  # Match in the middle
    EntranceRegister.objects.filter(authorized_requests__startswith=f'{REQUEST_TYPE_ENTRANCE},') |  # Match at the start
    EntranceRegister.objects.filter(authorized_requests__endswith(f',{REQUEST_TYPE_ENTRANCE}')) |  # Match at the end
    EntranceRegister.objects.filter(authorized_requests=f'{REQUEST_TYPE_ENTRANCE}')  # Exact match
)
