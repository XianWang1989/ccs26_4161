
entrance_registers = EntranceRegister.objects.filter(
    models.Q(authorized_requests__startswith=f"{REQUEST_TYPE_ENTRANCE},") |
    models.Q(authorized_requests__contains=f",{REQUEST_TYPE_ENTRANCE},") |
    models.Q(authorized_requests__endswith=f",{REQUEST_TYPE_ENTRANCE}") |
    models.Q(authorized_requests=f"{REQUEST_TYPE_ENTRANCE}")
)
