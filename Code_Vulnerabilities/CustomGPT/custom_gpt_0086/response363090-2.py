
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Use raw SQL with your custom function
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE regex_search(authorized_requests, %s)',
    [REGEX_ENTRANCE]
)
