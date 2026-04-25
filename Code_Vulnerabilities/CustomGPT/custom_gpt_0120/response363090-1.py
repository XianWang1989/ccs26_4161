
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
# Prepare the regex pattern
regex_pattern = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Use Q objects to create a fallback for SQLite
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__regex=regex_pattern) | 
    Q(authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE))
)

# If your data allows, ensure to adjust the matching logic as needed
