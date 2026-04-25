
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Custom filter using regex
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__regex=REGEX_ENTRANCE) | 
    Q(authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE))
)

# Convert to a list to evaluate in SQLite
entrance_registers_list = [register for register in entrance_registers if re.search(REGEX_ENTRANCE, register.authorized_requests)]
