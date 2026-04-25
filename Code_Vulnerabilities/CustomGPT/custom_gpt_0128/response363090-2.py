
from django.db.models import Func, F

class Regex(Func):
    function = 'regex'

entrance_registers = EntranceRegister.objects.annotate(
    match=Regex(str(REGEX_ENTRANCE), F('authorized_requests'))
).filter(match=True)
