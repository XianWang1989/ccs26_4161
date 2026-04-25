
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all entrance registers and filter using Python's regex
entrance_registers = EntranceRegister.objects.all()
filtered_registers = [
    register for register in entrance_registers
    if re.match(REGEX_ENTRANCE, register.authorized_requests)
]

# Now, filtered_registers contains the entries that match the regex
