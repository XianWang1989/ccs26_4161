
from django.db.models import Q
from django.db.models import CharField
from django.db.models.functions import Cast

# Define the request type
REQUEST_TYPE_ENTRANCE = 1

# Prepare your search terms
search_pattern = f",{REQUEST_TYPE_ENTRANCE},"

# Create a filter
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__startswith=f"{REQUEST_TYPE_ENTRANCE},") |
    Q(authorized_requests__endswith=f",{REQUEST_TYPE_ENTRANCE}") |
    Q(authorized_requests__contains=search_pattern) |
    Q(authorized_requests=f"{REQUEST_TYPE_ENTRANCE}")
).distinct()
