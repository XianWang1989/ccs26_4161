
import re
from your_app.models import EntranceRegister

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Use the REGEXP operator in your query
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__regex=REGEX_ENTRANCE
)
