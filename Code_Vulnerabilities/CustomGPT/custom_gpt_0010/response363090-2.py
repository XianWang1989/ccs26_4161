
from django.db.models import Func

class Regexp(Func):
    function = 'REGEXP'

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Ensure to activate the SQLite regex function
activate_sqlite_regex()

entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__regex=REGEX_ENTRANCE
)
