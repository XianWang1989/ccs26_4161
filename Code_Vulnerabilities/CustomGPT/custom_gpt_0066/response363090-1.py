
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all entrance registers and filter in Python
entrance_registers = EntranceRegister.objects.all()
filtered_registers = [
    register for register in entrance_registers
    if re.search(REGEX_ENTRANCE, register.authorized_requests)
]

# Alternatively, if the dataset is large, consider using Q objects for dynamic queries.
# This won't use regex but matches specific patterns.
query = Q()
for pattern in [f'^{REQUEST_TYPE_ENTRANCE}$', f',{REQUEST_TYPE_ENTRANCE},', f',{REQUEST_TYPE_ENTRANCE}$']:
    query |= Q(authorized_requests__icontains=pattern)

entrance_registers_q = EntranceRegister.objects.filter(query)
