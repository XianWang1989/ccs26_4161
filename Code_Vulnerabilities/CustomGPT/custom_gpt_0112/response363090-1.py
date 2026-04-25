
REQUEST_TYPE_ENTRANCE = 1
pattern = '{0},%|%,{0},%|%,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Using Q objects to build OR conditions
from django.db.models import Q

entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__startswith=f'{REQUEST_TYPE_ENTRANCE},') |
    Q(authorized_requests__endswith=f',{REQUEST_TYPE_ENTRANCE}') |
    Q(authorized_requests__contains=f',{REQUEST_TYPE_ENTRANCE},') |
    Q(authorized_requests=f'{REQUEST_TYPE_ENTRANCE}')
)
