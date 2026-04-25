
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
# Create patterns for LIKE queries
patterns = [
    f'{REQUEST_TYPE_ENTRANCE},%',
    f', {REQUEST_TYPE_ENTRANCE},',
    f', {REQUEST_TYPE_ENTRANCE}',
    f'{REQUEST_TYPE_ENTRANCE}'  # Matches just the number
]

# Build a Q object with OR conditions
query = Q()
for pattern in patterns:
    query |= Q(authorized_requests__contains=pattern)

# Execute the query
entrance_registers = EntranceRegister.objects.filter(query)
