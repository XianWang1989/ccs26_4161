
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Use the custom REGEXP function
entrance_registers = EntranceRegister.objects.extra(
    where=["authorized_requests REGEXP %s"],
    params=[REGEX_ENTRANCE]
)
