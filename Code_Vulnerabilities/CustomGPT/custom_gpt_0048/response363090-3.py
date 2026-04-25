
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__regex=REGEX_ENTRANCE
)
