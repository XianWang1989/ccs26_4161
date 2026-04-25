
REQUEST_TYPE_ENTRANCE = '1'  # as a string for LIKE

# Build the LIKE pattern
like_pattern = '%{}%'.format(REQUEST_TYPE_ENTRANCE)

# Use Q objects to handle multiple LIKE conditions
from django.db.models import Q

entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=REQUEST_TYPE_ENTRANCE) | 
    Q(authorized_requests__exact=REQUEST_TYPE_ENTRANCE)
)
