
import re

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

all_registers = EntranceRegister.objects.all()
entrance_registers = [reg for reg in all_registers if re.search(REGEX_ENTRANCE, reg.authorized_requests)]
