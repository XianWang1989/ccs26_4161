
from django.db.models import Func, F

class Regex(Func):
    function = 'REGEXP'

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    F('authorized_requests').regex(REGEX_ENTRANCE)
)
