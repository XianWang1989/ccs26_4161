
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__regex=REGEX_ENTRANCE)
)

# Example: Print the query
print(entrance_registers.query)
