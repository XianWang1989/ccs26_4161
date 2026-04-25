
from django.db.models import Func

class Regex(Func):
    function = 'regex'

# Usage in your query
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.annotate(
    regex_match=Regex('authorized_requests', REGEX_ENTRANCE)
).filter(regex_match=1)
