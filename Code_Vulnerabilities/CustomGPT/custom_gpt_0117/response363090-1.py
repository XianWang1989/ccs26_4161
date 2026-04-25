
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
request_str = str(REQUEST_TYPE_ENTRANCE)

# Constructing Q objects for the equivalent LIKE conditions
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__startswith=request_str + ',') |  # ,1
    Q(authorized_requests__contains=',' + request_str + ',') |  # ,1,
    Q(authorized_requests__endswith=',' + request_str) |  # ,1
    Q(authorized_requests=request_str)  # 1
)
