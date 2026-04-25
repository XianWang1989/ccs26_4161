
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
pattern = f"%{REQUEST_TYPE_ENTRANCE}%"
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__contains=REQUEST_TYPE_ENTRANCE) |
    Q(authorized_requests__startswith=REQUEST_TYPE_ENTRANCE) |
    Q(authorized_requests__endswith=REQUEST_TYPE_ENTRANCE)
)
