
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all entries and filter in Python
entrance_registers = EntranceRegister.objects.all().filter(
    Q(authorized_requests__contains=str(REQUEST_TYPE_ENTRANCE))
)

# Custom filtering in Python
filtered_registers = [
    register for register in entrance_registers 
    if re.match(REGEX_ENTRANCE, register.authorized_requests)
]

# Use `filtered_registers` as needed
