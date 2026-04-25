
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Get all entrance registers first
entrance_registers_queryset = EntranceRegister.objects.all()

# Filter using Python regex
entrance_registers = [
    register for register in entrance_registers_queryset
    if re.search(REGEX_ENTRANCE, register.authorized_requests)
]

# Now `entrance_registers` contains the filtered results
