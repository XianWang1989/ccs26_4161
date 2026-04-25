
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
request_str = str(REQUEST_TYPE_ENTRANCE)

# Build the query for SQLite
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=f',{request_str},') |
    Q(authorized_requests__icontains=f'{request_str},') |
    Q(authorized_requests__icontains=f',{request_str}') |
    Q(authorized_requests=request_str)
)
