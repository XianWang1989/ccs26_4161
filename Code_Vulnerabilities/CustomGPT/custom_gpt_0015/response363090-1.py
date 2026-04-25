
import re
from django.db import models
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
pattern = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all the records and filter in Python
entrance_registers = EntranceRegister.objects.all()
entrance_registers = [
    register for register in entrance_registers
    if re.search(pattern, register.authorized_requests)
]

# Or if the pattern is simpler, use the Q object for icontains
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE))
)
