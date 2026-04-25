
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE},') |
    Q(authorized_requests__icontains=f'{REQUEST_TYPE_ENTRANCE},') |
    Q(authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE}') |
    Q(authorized_requests=f'{REQUEST_TYPE_ENTRANCE}')
)
