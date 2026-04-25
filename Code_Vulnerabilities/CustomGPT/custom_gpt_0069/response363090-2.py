
from django.db import connection

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

query = f"""
SELECT * FROM porter_entranceregister 
WHERE authorized_requests REGEXP '{REGEX_ENTRANCE}'
"""
with connection.cursor() as cursor:
    cursor.execute(query)
    entrance_registers = cursor.fetchall()
