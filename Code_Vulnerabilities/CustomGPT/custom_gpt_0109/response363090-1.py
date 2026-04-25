
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
pattern = '%{}%'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__contains=pattern)
)
