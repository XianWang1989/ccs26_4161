
from django.db.models import F

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    Regexp(REGEX_ENTRANCE, F('authorized_requests'))
)
