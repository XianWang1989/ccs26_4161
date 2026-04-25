
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
pattern = f'%{REQUEST_TYPE_ENTRANCE},%'

entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__startswith=f'{REQUEST_TYPE_ENTRANCE},') |
    Q(authorized_requests__endswith(f',{REQUEST_TYPE_ENTRANCE}')) |
    Q(authorized_requests__contains=f',{REQUEST_TYPE_ENTRANCE},') |
    Q(authorized_requests=f'{REQUEST_TYPE_ENTRANCE}')
)
