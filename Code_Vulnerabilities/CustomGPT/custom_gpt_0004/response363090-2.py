
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

if connection.vendor == 'sqlite':
    entrance_registers = EntranceRegister.objects.raw(
        'SELECT * FROM porter_entranceregister WHERE regexp(%s, authorized_requests)',
        [REGEX_ENTRANCE]
    )
else:
    entrance_registers = EntranceRegister.objects.filter(authorized_requests__regex=REGEX_ENTRANCE)
