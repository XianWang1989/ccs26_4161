
import re
from your_app.models import EntranceRegister

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Get all records and filter in Python
entrance_registers = EntranceRegister.objects.all()
filtered_registers = [
    register for register in entrance_registers 
    if re.match(REGEX_ENTRANCE, register.authorized_requests)
]
