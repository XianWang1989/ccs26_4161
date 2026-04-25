
from django.db.models import Func

class Regex(Func):
    function = 'REGEXP'
    template = '%(function)s(%(expressions)s)'

# Usage in your queryset
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Ensure you call create_regex_function() on application start, e.g., in ready() of AppConfig
entrance_registers = EntranceRegister.objects.annotate(
    regex_match=Regex('authorized_requests', REGEX_ENTRANCE)
).filter(regex_match=True)
