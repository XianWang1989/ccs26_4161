
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
# Construct the various conditions to match the authorized_requests field.
filter_conditions = (
    Q(authorized_requests__startswith=str(REQUEST_TYPE_ENTRANCE) + ',') |
    Q(authorized_requests__endswith=',' + str(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests__icontains=',' + str(REQUEST_TYPE_ENTRANCE) + ',') |
    Q(authorized_requests=str(REQUEST_TYPE_ENTRANCE))
)

entrance_registers = EntranceRegister.objects.filter(filter_conditions)
