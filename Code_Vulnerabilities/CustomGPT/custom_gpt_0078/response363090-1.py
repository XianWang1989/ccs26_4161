
import re
from django.db.models import Q

# Define your request type
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all entrance registers first (or use a more specific queryset if needed)
entrance_registers = EntranceRegister.objects.all()

# Filter using Python's regex
filtered_registers = [
    register for register in entrance_registers
    if re.search(REGEX_ENTRANCE, register.authorized_requests)
]

# Now filtered_registers contains the results you want
