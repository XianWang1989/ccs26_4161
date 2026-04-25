
from django.db.models import Func, Value

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

class Regexp(Func):
    function = 'REGEXP'
    template = '%(expressions)s'

# Use the custom function in your queryset
entrance_registers = EntranceRegister.objects.filter(
    Regexp('authorized_requests', Value(REGEX_ENTRANCE))
).order_by('-created_at')
