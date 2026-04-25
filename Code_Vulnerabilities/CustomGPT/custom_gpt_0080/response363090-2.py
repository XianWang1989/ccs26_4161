
import re

REQUEST_TYPE_ENTRANCE = '1'
entrance_registers = EntranceRegister.objects.all()

# Regex pattern
pattern = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Filter in Python using regex
filtered_registers = [register for register in entrance_registers if re.search(pattern, register.authorized_requests)]
