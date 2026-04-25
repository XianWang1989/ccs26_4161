
from django.db import connection

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Custom query using SQLite `LIKE` instead of regex
entrance_registers = EntranceRegister.objects.raw("""
    SELECT * FROM porter_entranceregister
    WHERE authorized_requests LIKE %s
    ORDER BY created_at DESC
""", [f'%{REQUEST_TYPE_ENTRANCE}%' if REQUEST_TYPE_ENTRANCE else ''])
