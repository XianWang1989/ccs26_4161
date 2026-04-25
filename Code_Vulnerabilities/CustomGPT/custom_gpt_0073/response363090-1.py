
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(
    REQUEST_TYPE_ENTRANCE
)

# Adjusting the query for SQLite
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__contains=str(REQUEST_TYPE_ENTRANCE))
)

# Filter using Python regex
filtered_registers = [register for register in entrance_registers if re.match(REGEX_ENTRANCE, register.authorized_requests)]
