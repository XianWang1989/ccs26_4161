
entrance_registers = EntranceRegister.objects.extra(
    where=["authorized_requests REGEXP %s"], params=[REGEX_ENTRANCE]
)
