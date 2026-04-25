
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1

# Construct a pattern to match the entrance request.
pattern = f"{REQUEST_TYPE_ENTRANCE}"  # e.g., "1"
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__exact=pattern) |
    Q(authorized_requests__icontains=f",{pattern},") |
    Q(authorized_requests__istartswith=f"{pattern},") |
    Q(authorized_requests__iendswith=f",{pattern}")
)

# If you want to see the SQL query being generated:
print(entrance_registers.query)
