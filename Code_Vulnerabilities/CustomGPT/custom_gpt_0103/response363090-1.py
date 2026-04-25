
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
pattern = f"%{REQUEST_TYPE_ENTRANCE}%"  # This will match anywhere in the string

# Adjusting the query for SQLite usage
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=REQUEST_TYPE_ENTRANCE)  # For partial match
)
