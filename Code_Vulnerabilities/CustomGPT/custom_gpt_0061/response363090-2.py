
from django.db.models import Func

class Regexp(Func):
    function = 'REGEXP'

# Use a raw SQL expression with LIKE as mentioned above or the custom regex function if necessary
entrance_registers = EntranceRegister.objects.annotate(
    match=Regexp('authorized_requests', f'^{REQUEST_TYPE_ENTRANCE},|,{REQUEST_TYPE_ENTRANCE},|,{REQUEST_TYPE_ENTRANCE}$|^{REQUEST_TYPE_ENTRANCE}$')
).filter(match=True)
