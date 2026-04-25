
from django.db import connection

def get_entrance_registers(request_type_entrance):
    regex_pattern = r'^{0},|,{0},|,{0}$|^{0}$'.format(request_type_entrance)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM porter_entranceregister 
            WHERE authorized_requests LIKE %s
        """, [f"%{request_type_entrance}%"])
        rows = cursor.fetchall()

    return rows

# Usage
REQUEST_TYPE_ENTRANCE = 1
entrance_registers = get_entrance_registers(REQUEST_TYPE_ENTRANCE)
