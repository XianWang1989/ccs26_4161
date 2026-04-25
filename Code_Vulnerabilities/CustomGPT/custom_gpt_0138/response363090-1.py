
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
regex_pattern = r'(^{0},|,{0},|,{0}$|^{0}$)'.format(REQUEST_TYPE_ENTRANCE)

# Create a Q object to find the records matching the pattern
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__contains=str(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests__startswith=str(REQUEST_TYPE_ENTRANCE) + ',') |
    Q(authorized_requests__endswith=',' + str(REQUEST_TYPE_ENTRANCE)) |
    Q(authorized_requests=str(REQUEST_TYPE_ENTRANCE))
)
