
from django.db.models import Func, F

class RegExp(Func):
    function = 'REGEXP'

# Register the connection (place this in your app's ready method)
connect_database()

REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.filter(
    RegExp(F('authorized_requests'), REGEX_ENTRANCE)
)
