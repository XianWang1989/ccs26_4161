
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all entrance registers
entrance_registers = EntranceRegister.objects.all()

# Filter using Python's regex
filtered_registers = [
    register for register in entrance_registers
    if re.match(REGEX_ENTRANCE, register.authorized_requests)
]

# Now filtered_registers contains the EntranceRegister instances
# that match the regex condition.
