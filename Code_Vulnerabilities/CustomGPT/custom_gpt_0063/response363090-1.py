
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE},') |  # matches ",1,"
    Q(authorized_requests__startswith=f'{REQUEST_TYPE_ENTRANCE},') |  # matches "1,"
    Q(authorized_requests__endswith=f',{REQUEST_TYPE_ENTRANCE}') |  # matches ",1"
    Q(authorized_requests=f'{REQUEST_TYPE_ENTRANCE}')  # matches "1"
)
