
from django.db.models import Func, F

class RegexMatch(Func):
    function = 'regex_match'
    template = "%(function)s(%(expressions)s)"

# Usage
entrance_registers = EntranceRegister.objects.annotate(
    matches=RegexMatch(F('authorized_requests'), REGEX_ENTRANCE)
).filter(matches=True)
