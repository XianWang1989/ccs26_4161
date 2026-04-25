
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests__istartswith=str(REQUEST_TYPE_ENTRANCE) + ',') |
    Q(authorized_requests__iendswith=',' + str(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests=str(REQUEST_TYPE_ENTRANCE))
)
