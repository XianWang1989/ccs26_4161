
from myapp.models import EntranceRegister

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# This should work now in both PostgreSQL and SQLite with the registered function.
entrance_registers = EntranceRegister.objects.filter(authorized_requests__regex=REGEX_ENTRANCE)
