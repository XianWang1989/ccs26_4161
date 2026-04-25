
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
LIKE_ENTRANCE = '%{0}%'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=LIKE_ENTRANCE) |
    Q(authorized_requests=REQUEST_TYPE_ENTRANCE)
)

print(entrance_registers.query)
