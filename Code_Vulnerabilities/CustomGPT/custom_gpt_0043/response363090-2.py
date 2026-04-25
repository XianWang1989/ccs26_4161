
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Use raw SQL to filter using the custom regex function
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE regexp(%s, authorized_requests)', [REGEX_ENTRANCE]
)
