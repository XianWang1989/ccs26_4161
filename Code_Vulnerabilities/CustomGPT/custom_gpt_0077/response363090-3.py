
from django.db import connection

create_regex_function()  # Call this function where you're setting up.

REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__regex=REGEX_ENTRANCE
)
