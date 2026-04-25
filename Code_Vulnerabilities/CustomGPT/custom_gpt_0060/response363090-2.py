
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# First, get all EntranceRegisters
entrance_registers = EntranceRegister.objects.all()

# Then filter using Python's regex
filtered_entrance_registers = [
    entry for entry in entrance_registers if re.search(REGEX_ENTRANCE, entry.authorized_requests)
]

# Now filtered_entrance_registers contains the desired results.
