
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
# Create a pattern for LIKE queries
pattern = f'{REQUEST_TYPE_ENTRANCE},%'  # Matches {1}, any following string
pattern2 = f'%,{REQUEST_TYPE_ENTRANCE},%'  # Matches ,{1}, anywhere in the middle
pattern3 = f'%,{REQUEST_TYPE_ENTRANCE}'  # Matches ,{1} at the end
pattern4 = f'{REQUEST_TYPE_ENTRANCE}'  # Matches {1} on its own

# Use Q objects to perform the OR query
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=pattern) |
    Q(authorized_requests__icontains=pattern2) |
    Q(authorized_requests__icontains=pattern3) |
    Q(authorized_requests__icontains=pattern4)
)

# Print the resulting SQL query
print(entrance_registers.query)
