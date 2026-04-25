
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Get all records and filter with regex
entrance_registers = [
    register for register in EntranceRegister.objects.all()
    if re.search(REGEX_ENTRANCE, register.authorized_requests)
]
