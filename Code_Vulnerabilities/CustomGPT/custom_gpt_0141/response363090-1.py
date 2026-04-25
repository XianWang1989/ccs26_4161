
import re
from django.db.models import Q
from your_app.models import EntranceRegister

REQUEST_TYPE_ENTRANCE = 1
# Create a regex pattern to match the request type in a comma-separated format
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all entrance registers
entrance_registers = EntranceRegister.objects.all()

# Use Python's regex to filter results
filtered_registers = [
    register for register in entrance_registers 
    if re.search(REGEX_ENTRANCE, register.authorized_requests)
]

# Or using Q objects in a more Django-like way (less efficient for large datasets)
# If `authorized_requests` is a string field:
query_filter = Q()
query_filter |= Q(authorized_requests__exact=str(REQUEST_TYPE_ENTRANCE))
query_filter |= Q(authorized_requests__contains=f',{REQUEST_TYPE_ENTRANCE},')
query_filter |= Q(authorized_requests__contains=f',{REQUEST_TYPE_ENTRANCE}')
query_filter |= Q(authorized_requests__contains=f'{REQUEST_TYPE_ENTRANCE},')

entrance_registers_with_q = EntranceRegister.objects.filter(query_filter)

# Example output
for register in filtered_registers:
    print(register)

# Output using Q
for register in entrance_registers_with_q:
    print(register)
