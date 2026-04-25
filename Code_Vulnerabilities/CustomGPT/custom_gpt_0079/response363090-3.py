
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE regex(authorized_requests, %s)',
    [REGEX_ENTRANCE]
)
