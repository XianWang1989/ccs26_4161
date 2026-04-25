
import re

entrance_registers = EntranceRegister.objects.all()
pattern = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

filtered_registers = [register for register in entrance_registers if re.search(pattern, register.authorized_requests)]
