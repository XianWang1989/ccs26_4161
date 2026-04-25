
import re
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Create a custom filter function
def regex_filter(requests, regex):
    return [request for request in requests if re.search(regex, request)]

# Get all EntranceRegister objects
entrance_registers = EntranceRegister.objects.all()
filtered_registers = [entry for entry in entrance_registers if regex_filter(entry.authorized_requests, REGEX_ENTRANCE)]

# Now, filtered_registers will contain the desired results
