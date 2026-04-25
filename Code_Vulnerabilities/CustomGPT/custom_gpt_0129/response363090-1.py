
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
pattern = '{0},%,%,{0},%,%,{0}$%.'.format(REQUEST_TYPE_ENTRANCE)

# Using Q objects to build the query
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests__exact=str(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests__startswith=str(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests__endswith=str(REQUEST_TYPE_ENTRANCE))
)

# Note: You'll have to adapt the condition checks based on your use case.
