
from django.db.models import Func

class Regexp(Func):
    function = 'REGEXP'

# Use it in your query
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__regex=REGEX_ENTRANCE
)
