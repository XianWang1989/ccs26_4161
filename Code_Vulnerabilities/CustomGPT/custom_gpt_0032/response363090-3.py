
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.extra(
    where=[f"authorized_requests REGEXP '{REGEX_ENTRANCE}'"]
)
