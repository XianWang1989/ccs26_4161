
REQUEST_TYPE_ENTRANCE = '1'
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Ensure to call create_regex_function() before this line
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP ?', [REGEX_ENTRANCE]
)
