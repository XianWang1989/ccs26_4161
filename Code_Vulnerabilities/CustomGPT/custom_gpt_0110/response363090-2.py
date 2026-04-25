
import re

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Fetch all records
entrance_registers = EntranceRegister.objects.all()

# Filter using regex in Python
filtered_registers = [register for register in entrance_registers if re.search(REGEX_ENTRANCE, register.authorized_requests)]
