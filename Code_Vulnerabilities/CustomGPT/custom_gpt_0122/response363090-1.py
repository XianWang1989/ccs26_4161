
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
regex_pattern = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all records and filter using Python's regex
entrance_registers = EntranceRegister.objects.all()
filtered_registers = [
    reg for reg in entrance_registers
    if re.search(regex_pattern, reg.authorized_requests)
]
