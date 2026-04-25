
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
# Create patterns for LIKE
pattern = f"%{REQUEST_TYPE_ENTRANCE}%"

# Use Q objects to build the query
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=f',{REQUEST_TYPE_ENTRANCE},') |  # between commas
    Q(authorized_requests__startswith=f'{REQUEST_TYPE_ENTRANCE},') |  # starts with
    Q(authorized_requests__endswith=f',{REQUEST_TYPE_ENTRANCE}') |  # ends with
    Q(authorized_requests=f'{REQUEST_TYPE_ENTRANCE}')  # equals exactly
)

# Print the query for debugging
print(entrance_registers.query)
