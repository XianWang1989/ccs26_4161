
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
like_pattern = r'%{0}%'.format(REQUEST_TYPE_ENTRANCE)

# Constructing a Q object with LIKE
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=like_pattern)
)

# Note: `icontains` will perform case-insensitive matching.
